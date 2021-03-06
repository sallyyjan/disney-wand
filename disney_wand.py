"""tracks 'wand' object on webcam and displays its path"""
import numpy as np
import cv2

# output screen dimensions
frameWidth = 600
framHeight = 400
# output brightness
brightness = 150

# capture video from default camera (webcam)
vid = cv2.VideoCapture(index=0)
# set frame dimensions
vid.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, framHeight)
# set image brightness
vid.set(cv2.CAP_PROP_BRIGHTNESS, brightness)

# color range to detect the wand
# format [[low],[high]] as HSV values
wandColors = [[[5, 107, 0], [19, 255, 255]],
                [[133, 56, 0], [159, 156, 255]],
                [[57, 76, 0], [100, 255, 255]],
                [[90, 48, 0], [118, 255, 255]],] # could possibly be tuples?

# BGR values for paint colors of the wand
paintColors = [[51, 153, 255],          
                 [255, 0, 255],
                 [0, 255, 0],           
                 [255, 0, 0],]

# location and colour of paint
# [x , y , colorId ] 
myPoints = []  
imgResult = None

def detectWand(img, wandColors, paintColors):
    """return coordinates and color of each wand drawing"""

    # concerting BGR/RBG img to HSV format
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    wandCount = 0
    newPoints = []

    # get paint coordinates and color for each wand detected
    for color in wandColors:
        lower = np.array(color[0])
        upper = np.array(color[1])
        mask = cv2.inRange(imgHSV, lower, upper) # the binary image
        
        # get coordinates of wand
        x, y = getContours(mask) 

        # making the paint circles
        # TODO: check whether this is needed (same as drawOnCanvas)
        cv2.circle(imgResult, center=(x,y), radius=15, 
                    color=paintColors[wandCount], thickness=cv2.FILLED)
        
        if x != 0 and y != 0:
            newPoints.append([x,y,wandCount])
        wandCount += 1
    return newPoints

def getContours(img):
    """contours function with improved accuracy to get coordinate of wand point"""
    # mode: gets only exrteme outer contours
    # method: stores all contour points
    contours, hierarchy = cv2.findContours(img, mode=cv2.RETR_EXTERNAL,
                                                method=cv2.CHAIN_APPROX_NONE)
    
    x, y, w, h = 0, 0, 0, 0

    # improving accuracy of contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # assumes cnt with area > 500 is closed contour 
            perimeter = cv2.arcLength(cnt, True)

            # approximate polygonal curve of cnt
            # set max difference between original and approxCurve as 
            # 0.02 * perimeter
            approxCurve = cv2.approxPolyDP(cnt, 0.02 * perimeter, closed=True)
            
            x, y, w, h = cv2.boundingRect(approxCurve)
    # wand point is is center-left tip
    return x + (w // 2), y

def drawOnCanvas(myPoints, paintColors):
    """draws wand action on virtual canvas"""
    for point in myPoints:
        cv2.circle(imgResult, center=(point[0], point[1]), radius=10, 
                    color=paintColors[point[2]], thickness=cv2.FILLED)


while True:
    success, img = vid.read()
    imgResult = img.copy()

    newPoints = detectWand(img, wandColors, paintColors)

    # TODO: why need to copy then check length again?
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, paintColors)

    # display output on screen
    cv2.imshow("Result", imgResult)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

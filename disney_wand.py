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

def detectWand(img, wandColors, paintColors):
    """return coordinates and color of each wand drawing"""

    # concerting BGR/RBG img to HSV format
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    wandCount = 0
    newPoints = []

    # get paint coordinates and color for each wand detected
    for color in wandColors:
        lower = color[0]
        upper = color[1]
        mask = cv2.inRange(imgHSV, lower, upper) # the binary image
        x, y = getContours(mask) 

        # making the paint circles
        cv2.circle(imgResult, center=(x,y), radius=15, 
                    color=paintColors[wandCount], thickness=cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x,y,wandCount])
        
        count += 1
    
    return newPoints

def getContours():
    pass
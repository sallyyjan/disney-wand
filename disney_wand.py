"""tracks 'wand' on webcam and displays its path"""
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
# format [low],[high] as HSV values
wandColors = [[[5, 107, 0], [19, 255, 255]],
            [[133, 56, 0], [159, 156, 255]],
            [[57, 76, 0], [100, 255, 255]],
            [[90, 48, 0], [118, 255, 255]]] # could possibly be tuples?


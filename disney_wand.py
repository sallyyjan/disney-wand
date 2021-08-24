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

# 

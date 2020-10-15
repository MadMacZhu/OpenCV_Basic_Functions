import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

img = cv2.imread('data\messi5.jpg', 0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('TH1', 'Tracking', 0, 500, nothing)
cv2.createTrackbar('TH2', 'Tracking', 500, 500, nothing)


#canny = cv2.Canny(img, t1, t2) #2nd & 3rd arguments: threshold1, threshold2

#titles = ['image', 'canny']
#images = [img, canny]

while True:
    t1 = cv2.getTrackbarPos('TH1', 'Tracking')
    t2 = cv2.getTrackbarPos('TH2', 'Tracking')
    canny = cv2.Canny(img, t1, t2)
    cv2.imshow('image', img)
    cv2.imshow('canny', canny)

    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break


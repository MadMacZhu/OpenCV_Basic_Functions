import cv2
import numpy as np

img = cv2.imread('data\opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1, (0,255,0), 3) #-1 means drawing all contours
#print(len(contours))


cv2.imshow("image", img)
cv2.imshow("imgray", imgray)
cv2.waitKey()
cv2.destroyAllWindows()

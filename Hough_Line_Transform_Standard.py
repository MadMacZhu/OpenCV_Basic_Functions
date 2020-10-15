import cv2
import numpy as np

#Applying and finetuning the thresholds for Canny Edge Detection:
def nothing(x):
    pass
cv2.namedWindow('Tracking')
cv2.createTrackbar('Th1', 'Tracking', 50, 255, nothing)
cv2.createTrackbar('Th2', 'Tracking', 150, 255, nothing)


img = cv2.imread('data\sudoku.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    th1 = cv2.getTrackbarPos('Th1', 'Tracking')
    th2 = cv2.getTrackbarPos('Th2', 'Tracking')
    edges = cv2.Canny(imgray, th1, th2, apertureSize=3)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

#Applying the Standard Hough Line Transform:
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
#lines = cv2.HoughLines(image, rho, theta, threshold)
#lines: out put vector of lines. Each line is represented by a 2 or 3 element vector
#(rho, theta) or (rho, theta, votes). Rho is the distance3 from the coordinate origon;
#theta is the rotation angle in radians; votes is the value of accumulator.
#rho: distance resolution of the accumulator in pixels.
#theta: angle resolution of the accumulator in radians.
#threshold: accumulator threshold parameter. Only those lines are returned that get
#enough votes (> threshold).

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho

    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*a)
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*a)
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
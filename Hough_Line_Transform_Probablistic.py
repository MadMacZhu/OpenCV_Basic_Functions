import cv2
import numpy as np

#Applying and finetuning the thresholds for Canny Edge Detection:
def nothing(x):
    pass
cv2.namedWindow('Tracking')
cv2.createTrackbar('Th1', 'Tracking', 50, 255, nothing)
cv2.createTrackbar('Th2', 'Tracking', 150, 255, nothing)


img = cv2.imread('data\sudoku.png')
#img = cv2.imread('road.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:
    th1 = cv2.getTrackbarPos('Th1', 'Tracking')
    th2 = cv2.getTrackbarPos('Th2', 'Tracking')
    edges = cv2.Canny(imgray, th1, th2, apertureSize=3)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

#Applying the Probablistic Hough Line Transformation:
lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 100,
                        minLineLength = 100, maxLineGap = 10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

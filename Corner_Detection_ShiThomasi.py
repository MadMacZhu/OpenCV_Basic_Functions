import cv2
import numpy as np

img = cv2.imread('data\pic1.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(imgray, 25, 0.01, 10)
#Last 3 arguments:
#25 is the maximum number of corners
#0.01 is the quality level, i.e. the minimal expected quality corner
#10 is the min distance between returned corners.
corners = np.int0(corners) #int0 is actually int64

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('dst', img)
cv2.waitKey()
cv2.destroyAllWindows()


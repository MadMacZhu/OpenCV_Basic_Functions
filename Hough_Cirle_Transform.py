import cv2
import numpy as np

#img = cv2.imread('data\smarties.png')
img = cv2.imread('data\shapes.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray_blurred = cv2.medianBlur(imgray, ksize=5)
circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, dp=1,
                            minDist=20, param1=50, param2=30,
                            minRadius=0, maxRadius=0)
#The argumenst are: image, method
#dp: Inverse ratio of the accumulator resolution to the image resolution
#minDist: Minimum distance between the centers of the detected circles 
#param1: First method-specific parameter. In case of HOUGH_GRADIENT, it is
#the higher threshold of the two passed to the Canny edge detector.(The lower one is half.)
#param2: Second method-specific parameter. In case of HOUGH_GRADIENT, it is the
#accumulator threshold for the circle centers at the detection stage.
#minRadius: Minimum circle radius.
#maxRadius: Maximum circle radius. If <= 0, uses the maximum image dimension. If <  0,
#returns without finding the radius.

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(img, (x,y), r, (255,255,0), 3)
    cv2.circle(img, (x,y), 2, (255,255,0), 3)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
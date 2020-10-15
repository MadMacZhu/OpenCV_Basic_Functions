import numpy as np
import cv2

#img = cv2.imread('data\lena.jpg', 1)
#print(img.shape)
img = np.zeros([512, 512, 3], np.uint8)

img = cv2.line(img, (0,0) , (255,255), (255,255,0), 4)
img = cv2.arrowedLine(img, (0,255) , (255,255), (255,0,255), 4)
#Five arguments: image, pt1, pt2, color, width

img = cv2.rectangle(img, (0,300), (255,400), (0,0,255), 4)
#Five arguments: image, pt1.TL, pt2.BR, color, width (-1 for filled)

img = cv2.circle(img, (375,100), 100, (0,255,255),4)
#Five arguments: image, center, radius, color, width (-1 for filled)

img = cv2.putText(img, 'OpenCV', (275,275), cv2.FONT_HERSHEY_SIMPLEX, 2,
                  (255,255,255), 3, cv2.LINE_AA)
#Eight arguments: image, text, starting pt, font, fontsize, color, width, linetype.

cv2.imshow('lena', img)
cv2.waitKey()
cv2.destroyAllWindows()

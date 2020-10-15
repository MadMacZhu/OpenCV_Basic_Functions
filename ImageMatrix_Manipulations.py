import cv2
import numpy as np

img = cv2.imread('data\messi5.jpg')
img2 = cv2.imread('data\opencv-logo.png')

print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img2 = cv2.resize(img2, (548, 342))

#dstImage = cv2.add(img, img2)
dstImage = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
#dst = img*alpha + img2*beta + gamma

cv2.imshow("Messi", img)
cv2.imshow("DstImage", dstImage)
cv2.waitKey()
cv2.destroyAllWindows()

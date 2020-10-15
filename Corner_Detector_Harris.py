import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data\pic1.png')
original = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray = np.float32(imgray) #cv2.cornerHarris() only takes float32 type of images

dst = cv2.cornerHarris(imgray, blockSize=2, ksize=3, k=0.04)
#Last 3 arguments:
#blockSize: the size of neighbourhood considered for coner detection
#ksize: aperture parameter of Sobel derivative used.
#k: Harris detector free parameter in the equation.
dst = cv2.dilate(dst, None)
img[dst > 0.01 * dst.max()] = [0, 0, 255]

plt.subplot(121)
plt.imshow(img)
plt.title('dst')
plt.subplot(122)
plt.imshow(original)
plt.title('original')
plt.show()
#cv2.imshow('dst', img)
#cv2.imshow('original', original)
cv2.waitKey()
cv2.destroyAllWindows()

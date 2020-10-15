import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("data\smarties.png", 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=4)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #erosion followed by dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #dilation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
tophat =  cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 
          'gradient', 'tophat']
images = [img, mask, dilation, erosion, opening, closing, 
          mg, tophat]

for i in range(8):
    plt.subplot(3, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()


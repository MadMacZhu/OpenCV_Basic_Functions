import cv2
import numpy as np

img = cv2.imread('data\lena.jpg')

#lr1 = cv2.pyrDown(img)
#hr1 = cv2.pyrUp(lr1)

layer = img.copy()
gp = [layer]
for i in range(3):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

#Creating the Laplacian pyramid:
lp = []
for i in range(3):
    gaussian_ext = cv2.pyrUp(gp[i+1])
    lp_layer = cv2.subtract(gp[i], gaussian_ext)
    lp.append(lp_layer)
    cv2.imshow(str(i), lp_layer)

print(len(lp))

#cv2.imshow('Original image', img)
#cv2.imshow('pyrDown1', lr1)
#cv2.imshow('pyrUp1', hr1)
cv2.waitKey(0)
cv2.destroyAllWindows()
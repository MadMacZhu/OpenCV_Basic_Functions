import cv2
import numpy as np

apple = cv2.imread('apple.jpg', 1)
orange = cv2.imread('data\orange.jpg', 1)
#print(apple.shape)
#print(orange.shape)
#apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

#Step 1: generating gaussian pyramids
layerA = apple.copy()
layerO = orange.copy()
gpA = [layerA]
gpO = [layerO]
for i in range(6):
    layerA = cv2.pyrDown(layerA)
    layerO = cv2.pyrDown(layerO)
    gpA.append(layerA), gpO.append(layerO)

#Step 2: generating Laplacian pyramids:
lpA = []
lpO = []
for i in range(6):
    tempA = cv2.pyrUp(gpA[i+1])
    tempO = cv2.pyrUp(gpO[i+1])
    lapA = cv2.subtract(gpA[i], tempA)
    lapO = cv2.subtract(gpO[i], tempO)
    lpA.append(lapA), lpO.append(lapO)

lpA.append(gpA[6]), lpO.append(gpO[6])

#Step 3: adding left and right halves of images in each level of Laplacian pyramid
apple_orange_pyramid = []
for lapA, lapO in zip(lpA, lpO):
    rows, cols, ch = lapA.shape
    apple_orange_add = np.hstack((lapA[:, :int(cols/2)], lapO[:, int(cols/2):]))
    apple_orange_pyramid.append(apple_orange_add)

#now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[6]
for i in range(6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_reconstruct, 
                                       apple_orange_pyramid[6-i-1])

#cv2.imshow("apple", apple)
#cv2.imshow("orange", orange)
#cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_add", apple_orange_reconstruct)

cv2.waitKey()
cv2.destroyAllWindows()

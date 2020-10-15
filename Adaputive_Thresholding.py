import cv2
import numpy as np

img = cv2.imread('data\sudoku.png', 0)

_, simp_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adpt_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
adpt_threshG = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 11, 2)
#The last two parameters are: blocksize, c-value.

cv2.imshow("Image", img)
cv2.imshow("SimpThresh", simp_thresh)
cv2.imshow("AdptThresh", adpt_thresh)
cv2.imshow("AdptThreshGaussian", adpt_threshG)

cv2.waitKey()
cv2.destroyAllWindows()
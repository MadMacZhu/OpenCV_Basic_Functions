import cv2
import numpy as np

img1 = np.zeros((250, 500, 3), dtype=np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2 = np.zeros((250,500,3), dtype=np.uint8)
img2 = cv2.rectangle(img2, (0,0), (250,500), (255,255,255), -1)

bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitNot = cv2.bitwise_not(img1)
bitXor = cv2.bitwise_xor(img2, img1) #1 xor 1 = 0, 0 xor 1 = 1

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitNot", bitNot)
cv2.imshow("bitXor", bitXor)

cv2.waitKey()
cv2.destroyAllWindows()
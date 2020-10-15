import cv2
import numpy as np

img = cv2.imread('data\smarties.png')
imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread('data\smarties_one.png', 0)
w, h = template.shape[::-1]

#print(img.shape)
#print(template.shape)
res = cv2.matchTemplate(imgrey, template, cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.990
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h), (0,0,255), 2)


cv2.imshow("image", img)
cv2.waitKey()
cv2.destroyAllWindows()
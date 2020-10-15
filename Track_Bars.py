import cv2
import numpy as np

def nothing(x):
    print(x)
#Previous a callback function

#img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

#cv2.createTrackbar('B', 'image', 0, 255, nothing)
#cv2.createTrackbar('G', 'image', 0, 255, nothing)
#cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('CP', 'image', 10, 400, nothing)

#switch = '0: OFF\n 1: ON'
switch = 'color/gray'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(True):
    img = cv2.imread('data\lena.jpg')
    k =cv2.waitKey(1)
    if k == 27:
        break

    #b = cv2.getTrackbarPos('B', 'image')
    #g = cv2.getTrackbarPos('G', 'image')
    #r = cv2.getTrackbarPos('R', 'image')
    pos = cv2.getTrackbarPos('CP', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0,0,255), 2)

    if s == 0:
        #img[:] = 0
        pass
    elif s == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('image', img)

cv2.destroyAllWindows()

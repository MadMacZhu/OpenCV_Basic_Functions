import cv2
import numpy as np

#events = [i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ', y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,0), 2)
        cv2.imshow('Image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, strBGR, (x,y), font, 0.5, (0,255,0),2)
        cv2.imshow('Image', img)

    if event == cv2.EVENT_RBUTTONUP:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x,y), 3, (0,255,0), -1)
        mycolorImage = np.zeros((512, 512, 3), np.uint8)
        mycolorImage[:] = [blue, green, red]
        cv2.imshow('Color', mycolorImage)


    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,0), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0,0,0), 5)
        cv2.imshow('Image', img)

#img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread('data\lena.jpg', 1)
points = []
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)

cv2.waitKey()
cv2.destroyAllWindows()
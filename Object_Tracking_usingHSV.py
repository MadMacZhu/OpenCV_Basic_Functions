import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_H = cv2.getTrackbarPos('LH', 'Tracking')
    upper_H = cv2.getTrackbarPos('UH', 'Tracking')
    lower_S = cv2.getTrackbarPos('LS', 'Tracking')
    upper_S = cv2.getTrackbarPos('US', 'Tracking')
    lower_V = cv2.getTrackbarPos('LV', 'Tracking')
    upper_V = cv2.getTrackbarPos('UV', 'Tracking')

    
    lower_B = np.array([lower_H, lower_S, lower_V])
    upper_B = np.array([upper_H, upper_S, upper_V])

    mask = cv2.inRange(hsv, lower_B, upper_B)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
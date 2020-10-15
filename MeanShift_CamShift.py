import cv2
import numpy as np
from matplotlib import pylab as plt

cap = cv2.VideoCapture('Car.mp4')

#take the first frame of the video
ret, frame = cap.read()
#plt.imshow(frame)
#plt.show()
#setup the initial ROI for tracking
x, y, w, h = 700, 350, 100, 100
track_window = (x, y, w, h)
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist, roi_hist, 0, 255, norm_type=cv2.NORM_MINMAX)
#setup the termination criteria, either 10 iterations or move by at least 1 pt
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],1)
    #apply meanshift to get the new location
    #ret, track_window = cv2.meanShift(dst, track_window, term_crit)
    ret, track_window = cv2.CamShift(dst, track_window, term_crit)
    #draw it on image
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    final_image = cv2.polylines(frame, [pts], True, (0, 255, 0), 3)
    #x, y, w, h = track_window
    #final_image = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    cv2.imshow('final_image', final_image)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

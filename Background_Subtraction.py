import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
#The detectShadows method is optional.
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False) #Similarly the parameter is optional

#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
#kernel combined with morphologyEx is for reducing noises.

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    fgmasked = fgbg.apply(frame)
    #fgmasked = cv2.morphologyEx(fgmasked, cv2.MORPH_OPEN, kernel)
    #fgmasked = cv2.cvtColor(fgmasked, cv2.COLOR_GRAY2BGR)
    #frame = cv2.bitwise_and(frame, fgmasked)
    #Uncomment the above two lines to apply the mask to the original frame

    cv2.imshow('FG MASKED frame', fgmasked)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

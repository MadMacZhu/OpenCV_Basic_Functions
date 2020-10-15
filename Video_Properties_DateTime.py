import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #Can use 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #Can use 4

#cap.set(3, 400) #Camera will only set the resolution to what's available to it.
#cap.set(4, 300)

#print(cap.get(3))
#print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Width: " + str(cap.get(3)) + " Height: " + str(cap.get(4))
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
    frame = cv2.putText(frame, datet, (10,200), font, 1, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

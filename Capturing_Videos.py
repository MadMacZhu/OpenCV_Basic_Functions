import cv2

#Capturing videos:
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#Reading videos

vid = cv2.VideoCapture("vtest.avi")
out = cv2.VideoWriter("Vout.avi", cv2.VideoWriter_fourcc(*'XVID'), 30, (768,576))

while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == False:
        break
    
    cv2.imshow('video', frame)
    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break
    elif frame is None:
        break

width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(str(width) +' '+str(height))

vid.release()
out.release()
cv2.destroyAllWindows()


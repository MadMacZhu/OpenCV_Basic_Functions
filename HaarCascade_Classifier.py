import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('data\ml.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
#The last two arguments:
#scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
#minNeighbors: Parameter specifying how many neighbors each candidate rectangle
#should have to retain it.

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

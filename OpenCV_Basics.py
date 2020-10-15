import cv2

img = cv2.imread("data\lena.jpg", 0) #Flags:1 - color; 0 - grayscale; -1 - including alpha channel

cv2.imshow("lena", img)
key = cv2.waitKey()

if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('lennna.png', img)
    cv2.destroyAllWindows()
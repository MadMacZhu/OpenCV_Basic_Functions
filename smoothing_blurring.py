import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('data\water.png')
img = cv2.imread('data\lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), dtype=np.float32)/25

dst = cv2.filter2D(img, -1, kernel) #Second argument is depth
blur = cv2.blur(img, (5,5))
gaussianblur = cv2.GaussianBlur(img, (5,5), sigmaX = 0)
#Gaussian blur is designed to remove high frequency noise from the image
median = cv2.medianBlur(img, 5)
#median blur is designed to remove salt-n-pepper noise (black and white dots noise)
bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)
#4 arguments: image, diameter, sigmaColor, sigmaSpace

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 
          'MedianBlur', 'BilateralFiter']
images = [img, dst, blur, gaussianblur,
         median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

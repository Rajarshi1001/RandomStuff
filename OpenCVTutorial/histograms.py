import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blank=np.zeros(img.shape[:2],dtype='uint8')
circle=cv.circle(blank.copy(),(gray.shape[1]//2-45,gray.shape[0]//2), 100, 255, -1)
mask=cv.bitwise_and(gray, gray , mask=circle)
cv.imshow('masked_image', mask)
#cv.imshow('grayscale',gray)
#histogram for the grayscale image
gray_hist=cv.calcHist([gray],[0],mask, [256], [0,256])#histogram for the masked image

plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist) # plots the histogram that depicts the pixel distribution of the image
plt.xlim([0,256])
plt.show() # displays the histogram

#histogram for coloured image

colors={'b','g','r'} #opencv interprets image in the bgr format
for i,col in enumerate(colors):
    coloured_hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(coloured_hist,color=col)
    plt.xlim([0,256])
plt.title('Coloured Histogram')   
plt.show()

cv.waitKey(0)    

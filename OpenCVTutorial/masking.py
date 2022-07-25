import cv2 as cv
import numpy as np
#masking the images using bitwise operations
img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
blank=np.zeros((img.shape[0],img.shape[1]), dtype='uint8')
#creating a mask
circle=cv.circle(blank.copy(),(img.shape[1]//2-45, img.shape[0]//2),100, 255, -1)
#cv.imshow('mask', circle)
masked_img=cv.bitwise_and(img,img,mask=circle)# masks the image inside the circle 
cv.imshow('masked_image',masked_img)

cv.waitKey(0)
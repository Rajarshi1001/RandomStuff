import cv2 as cv
import numpy as np
#binarising the image
#There are two types of thresholding- Simple Thresh holding and adpated thresholding
img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh=cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#thresh stores the thresholded image and threshold stores the threshold value passed by the user(i.e 150)
cv.imshow('Simple_thresholded_image',thresh)
threshold, thresh_inv=cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse_Simple_hresholded_image',thresh_inv)

#adaptive thresholding
thresh_adp=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('Adapted_thresholded_image',thresh_adp)

cv.waitKey(0)
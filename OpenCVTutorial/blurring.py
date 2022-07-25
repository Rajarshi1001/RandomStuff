#methods of blurring
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
cv.imshow('normal_image',img)
avg=cv.blur(img,(7,7))#average blurring
cv.imshow('average_blurred_image',avg)
gauss=cv.GaussianBlur(img,(7,7),0,cv.BORDER_DEFAULT)#Gaussian blurring is more realistic than average blurring and extent of blurring is less than average blurring
cv.imshow('gaussian_blurred_image',gauss)
med=cv.medianBlur(img,7)#median blurring
cv.imshow('median_blurred_image',med)
blb=cv.bilateralFilter(img,15, 25,25)#bilateral blurring....most effective for retaining the edged of the image
cv.imshow('bilateral_blurred_image',blb)
cv.waitKey(0)
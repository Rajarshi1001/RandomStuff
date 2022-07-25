import cv2 as cv
import numpy as np
#a pixel is turned on if it a value of 1 and turned off if it has a value of 0
blank=np.zeros((400,400), dtype='uint8')
rect=cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle=cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('circle', circle)
cv.imshow('rectangle', rect)

im=cv.bitwise_and(rect, circle)#calculates the intersection of the two images
cv.imshow('bitwise_and',im)

im2=cv.bitwise_or(rect, circle)#calculates the union of the two images
cv.imshow('bitwise_or',im2)

im3=cv.bitwise_xor(rect, circle)#calculates the non intersecting regions of the two images
cv.imshow('bitwise_xor',im3)

im4=cv.bitwise_not(rect)#basically inverts the binary colour of the image. black converted to white and vice-versa
cv.imshow('bitwise_not_rectangle',im4)

cv.waitKey(0)
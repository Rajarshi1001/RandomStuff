import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.resize(cv.imread('people.jpg'), (0,0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
haar_cascade=cv.CascadeClassifier('haar_frontalface.xml')# reading the xml file and string in the haar_cascade variable
haar=cv.CascadeClassifier('haar_eyes.xml')
faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)#creation of an object and paaing the detectmultiscale function to the object and draws a rectangle around the face and returns  a tuple of starting coordinates and width, height.
print(len(faces_rect))

for(x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
    gray_cropped=gray[x:x+w,y:y+h]
    eyes=haar.detectMultiScale(gray_cropped, scaleFactor=1.1, minNeighbors=3)
    
    for(a,b,c,d) in eyes:
        cv.rectangle(img, (a,b), (a+w,b+h), (0,255,0), 3)
    
cv.imshow('detected_face', img)    
     
cv.imshow('grayscale',gray)
cv.waitKey(0)
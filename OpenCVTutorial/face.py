import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.resize(cv2.imread('h3.jpg'), (0,0), fx=0.9, fy=0.9)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

haar = cv2.CascadeClassifier("haar_eyes.xml")
eyes = haar.detectMultiScale(gray)[1]
print(eyes)
(eye_x, eye_y,w,h) = eyes

cv2.rectangle(img, (eye_x, eye_y),(w,h),(255,0,0),-1)
cv2.imshow('Hermione',img)
cv2.waitKey(0)
cv2.destroyAllwindows()

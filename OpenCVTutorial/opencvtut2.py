import cv2 as cv
import numpy as np
import random

blank=np.zeros((500,500,3), dtype='uint8')
im=cv.imread('pokeon.jpg')
img=cv.resize(cv.imread('pokeon.jpg'), (0,0), fx=0.2, fy=0.2,interpolation=cv.INTER_AREA)
#cv.rectangle(blank,(0,0),(blank.shape[0]//3,blank.shape[1]//3),(34,47,132),thickness=-1)
#cv.circle(blank,(blank.shape[0]//3,blank.shape[1]//3),30,(34,47,132),thickness=-1)
"""
im=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)#blurring an  image,
edge=cv.Canny(img, 125, 175)
dilate=cv.dilate(edge,(7,7),iterations=3)
eroded=cv.erode(edge,(7,7), iterations=3)
cv.imshow('Eroded_image',eroded)
cv.imshow('Dilated_image',dilate)
"""

def translate(img, x,y):
    TranslateMat=np.float32([[1,0,x],[0,1,y]])#takes a 2x3 translation matrix
    dim=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,TranslateMat,dim)#transformational functions
    
def rotate(img,angle,rotPoint=None):
    width, height=img.shape[1], img.shape[0]
    dim=(width,height)
    if rotPoint==None:
        rotPoint=(img.shape[1]//2,img.shape[0]//2)
    rotateMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)    
    return cv.warpAffine(img,rotateMat,dim)
x=0 
y=0
theta=0
while True:
   im2=translate(img,x,y)
   im2=rotate(img,theta)   
   cv.imshow('translate&rotate_image',im2)   
   x=x+random.randint(-1,1)
   y=y+random.randint(-1,1)
   theta=random.randint(0,360)
   if cv.waitKey(50) & 0xFF==ord('a'):
      break
#cv.imshow('Edges',edge)
#cv.imshow('clear_image',img)
#cv.imshow('blurred_image', blur)
#cv.waitKey(0)
cv.destroyAllWindows()

"""
fliped=cv.flip(img,1)
cv.imshow('Flip',fliped)
cropped_image=img[100:400, 200:400]
cv.imshow('Cropped',cropped_image)
"""
cv.waitKey(0)
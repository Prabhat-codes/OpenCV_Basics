import cv2 as cv
import numpy as np 

img=cv.imread('/home/prabhat/Desktop/Code/OpenCV_Basics/Photos/park.jpg')
cv.imshow('Boston',img)

#converting an image to grayscale
#BGR to greyscale
grey=cv.cvtColor(img, cv.COLOR_BGR2GRAY )
cv.imshow('grey',grey)  

#Blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny=cv.Canny(blur, 125, 175)
cv.imshow('Canny image',canny)

#Dilating images
dilated=cv.dilate(canny, (8,8),iterations=1)
cv.imshow("Dilated",dilated)

#eroding
eroded=cv.erode(dilated,(9,9),iterations=1)
cv.imshow("Eroded",eroded)

#resize
resized=cv.resize(eroded,(500,500))
#interpolation=cv.INTER_AREA to compress and cv.INTER_LINEAR/CUBIC for enlarging at good quality 
cv.imshow("Resized",resized)

#cropping
cropped=img[50:300,20:400]
cv.imshow("Cropped",cropped)
cv.waitKey(0)
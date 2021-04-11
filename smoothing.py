import cv2 as cv 
import numpy as np 

img=cv.imread('Photos\cats.jpg')
cv.imshow("Img",img)

#Averaging 

average=cv.blur(img, (3,3))
cv.imshow("Average Blur",average)

#Gaussian blur
gaussian=cv.GaussianBlur(img,(3,3), 0)
cv.imshow("Gaussian Blur 0",gaussian)

#Median blur -> more effecting at removing noise than gaussian and average 
median=cv.medianBlur(img,7)
cv.imshow("Median Blur",median)

#Bilateral blurring 
bilateral=cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("bilateral",bilateral)
cv.waitKey(0)
import cv2 as cv
import numpy as np 
img=cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Laplacian 
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Lap",lap)

#sabel
sabelx=cv.Sobel(gray,cv.CV_64F, 1, 0)
sabely=cv.Sobel(gray,cv.CV_64F, 0, 1)
combined=cv.bitwise_or(sabelx,sabely)
cv.imshow("combined",combined)
cv.imshow("sabelx", sabelx)
cv.imshow("sabely",sabely)

#canny
canny=cv.Canny(gray, 150, 250 )
cv.imshow("Canny",canny)
canny1=cv.Canny(gray, 100, 250 )
cv.imshow("Canny1",canny1)
canny2=cv.Canny(gray, 150, 350 )
cv.imshow("Canny2",canny2)
cv.waitKey(0)

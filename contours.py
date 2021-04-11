import cv2 as cv
import numpy as np
img=cv.imread('Photos\cats.jpg')
cv.imshow("Normal",img)
blank=np.zeros(img.shape,dtype='uint8')
cv.imshow("blank",blank)

grey=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grey",grey)

blur=cv.GaussianBlur(grey,(5,5),cv.BORDER_DEFAULT)
canny=cv.Canny(blur,threshold1=125,threshold2=175)
cv.imshow("canny",canny)


ret,thresh=cv.threshold(canny,thresh=125,maxval=255,type=cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
#takes an image and converts it into binary form 
#if a pixel is below thresh, it is set to 0 
#if it is above thresh, it is set to 1/maxval


#findcontours

contours,heirarchies=cv.findContours(canny,mode=cv.RETR_LIST,method=cv.CHAIN_APPROX_SIMPLE)
#Retr list -> all the contours
#retr external -> only external 
#retr tree -> all heirarichal contours
#chain approx none -> how to approx the contours -> returns all contours
#chain approx simple -> compresses all contours into simple ones that makes sense    
print(len(contours), 'contours found')

cv.drawContours(blank,contours, -1,(0,0,255),thickness=1)
cv.imshow('Contours drawn',blank)


cv.waitKey(0)
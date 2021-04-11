import cv2 as cv 
import numpy as np 

img=cv.imread('Photos\park.jpg')
cv.imshow("Img",img)

blank=np.zeros(img.shape[0:2],dtype='uint8')
b,g,r=cv.split(img)

cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow("Merged",merged)
cv.waitKey(0)

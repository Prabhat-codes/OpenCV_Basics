import cv2 as cv 
import numpy as np 

img=cv.imread("Photos\cats 2.jpg")
blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Cats",img)
cv.imshow("blank",blank)

mas_c=cv.circle(blank.copy(), (img.shape[1]//2,(img.shape[0]//2)),100, 255, -1)
cv.imshow("mask_circ",mas_c)

mas_r=cv.rectangle(blank.copy(), (img.shape[1]//2,(img.shape[0]//2)),(img.shape[1]//2+100,(img.shape[0]//2+100)), 255, -1)
cv.imshow("mask_rec",mas_r)

wierd=cv.bitwise_and(mas_c,mas_r)
masked_img_r=cv.bitwise_and(img, img, mask=mas_r)
cv.imshow("masked image rectangle",masked_img_r)

masked_img_c=cv.bitwise_and(img, img, mask=mas_c)
cv.imshow("masked image circle",masked_img_c)

masked_img_w=cv.bitwise_and(img, img, mask=wierd)
cv.imshow("masked image wierd",masked_img_w)

cv.waitKey(0)

import cv2 as cv

img=cv.imread('Photos/cats.jpg')
cv.imshow("img",img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

#Simple thresholding
threshold,thresh=cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
#thresh -> the binarized image 
#threshold -> the value of thresholding
cv.imshow("thrsh",thresh)

threshold,thresh_inverse=cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
#thresh -> the binarized image 
#threshold -> the value of thresholding
cv.imshow("thrsh_inverse",thresh_inverse)

#adaptive thresholding
# let the computer find the optimal threshold value by itself
# in simple one we are doing it by ourselves so 
adaptive_thresh_g=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresh",adaptive_thresh_g)

adaptive_thresh_m=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresh m",adaptive_thresh_m)

adaptive_thresh_m1=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 8)
cv.imshow("adaptive thresh m1",adaptive_thresh_m1)
cv.waitKey(0)


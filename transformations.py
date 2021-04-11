import cv2 as cv
import  numpy as np 

img=cv.imread("Photos\park.jpg")

cv.imshow("Normal",img)

#translation
def translate(img, x, y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

    # -x --> left
    # +x --> up
    # -y -->Right
    # +y --> down
trans=translate(img, 100,100)
cv.imshow("Translate",trans)

#rotation 
def rotate(img, angle, rotPoint=None):
    (height, width)=img.shape[:2]

    if rotPoint==None: 
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions=(width,height)

    return cv.warpAffine(img,rotMat,dimensions)
rot=rotate(img,30,None)
cv.imshow("Rotated",rot)

# resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

#Flip
flip=cv.flip(img,flipCode=0)
# 0 means flipping vertically
# 1 means flipping horizontally
# -1 means flipping both vertically and horizontally
cv.imshow("flipped",flip)

#cropping
cropped=img[200:400,200:400]
cv.imshow("cropped",cropped)


cv.waitKey(0)
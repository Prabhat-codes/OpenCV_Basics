import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("Photos\cats.jpg")
cv.imshow("Img",img)

# plt.imshow(img)
# plt.show()

#convert bgr to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("grey",gray)

#convert bgr to hsv (hue saturation value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

#convert bgr to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)

#bgr to rgb
#All python libraries take in as RGB and open cv works on BGR so we have to 
#invert all the open cv images first so that its easier and more compatible with other languages
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
# plt.imshow(rgb) UNCOMMENT THIS IF YOU WANNA
# plt.show()

#HSV to bgr
hsv_bgr= cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow("hsv to bgr",hsv_bgr)

#HSV to bgr
lab_bgr= cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("lab to bgr",lab_bgr)


cv.waitKey(0)
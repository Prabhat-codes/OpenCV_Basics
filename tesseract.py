import cv2 as cv
import pytesseract 

def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

def grayscale(img):
    return cv.cvtColor(img,cv.COLOR_BGR2GRAY)

def noise(img):
    return cv.medianBlur(img,5)

def threshold(img):
    return cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)[1]


img=cv.imread("ocr_check.png")
img=grayscale(img)
img=threshold(img)
img=noise(img)
print(ocr_core(img))


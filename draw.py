import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
#1. Paint the image a certain color 

# blank[200:300, 300:400]=255,255,0
# cv.imshow('Blank',blank)

#2. Draw a rectangle 
#cv.rectangle(blank, (0,0), (40,240),(0,222,0),thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (250,250),(0,222,0),thickness=-1)
#cv.imshow('Rectangle',blank)
#3. Draw a circle
cv.circle(blank,(250,250), 100, (0,250,250),thickness=-1)

#4. Draw a line 
cv.line(blank, (0,0),(250,250),(255,0,0),thickness=23)


#5. Write text
cv.putText(blank,"hello, my name is prabhat",(225,225),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color=(0,0,255),thickness=2)
cv.imshow('Combination',blank)
cv.waitKey(0)
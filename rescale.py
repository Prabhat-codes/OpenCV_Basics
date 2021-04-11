import cv2 as cv
img=cv.imread("Photos\cat.jpg")


def rescaleFrame(frame, scale=0.75):
    #Images, Videos and Live Video
    width=int(frame.shape[1] * scale)
    height=int(frame.shape[0] * scale)
    
    dimensions=(width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width,height):
    #live Video 
    capture.set(3,width)
    capture.set(4,height)

resized_img=rescaleFrame(img)
cv.imshow('Catresized',resized_img)
cv.imshow('Cat',img)

capture=cv.VideoCapture('Videos/dog.mp4')
while True: 
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    cv.imshow('Video resized',frame_resized)
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0XFF==ord('d'):
        break
cv.waitKey(0)
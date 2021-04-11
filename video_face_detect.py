import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade=cv.CascadeClassifier('haar_face.xml')
    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor= 1.1,minNeighbors=  1)
    for x,y,w,h in faces_rect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv.imshow('detected faces',frame)
    # Display the resulting frame
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
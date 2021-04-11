import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    b,g,r=cv2.split(frame)

    blank=np.zeros(frame.shape[0:2],dtype='uint8')

    blue=cv2.merge([b,blank,blank])
    green=cv2.merge([blank,g,blank])
    red=cv2.merge([blank,blank,r])
    cv2.imshow("blue",blue)
    cv2.imshow("green",green)
    cv2.imshow("red",red)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
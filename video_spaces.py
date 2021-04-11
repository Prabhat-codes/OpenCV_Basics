import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("RGB",rgb)

    # lab=cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)
    # cv2.imshow("lab",lab)

    # hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv",hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
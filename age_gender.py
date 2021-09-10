import numpy as np
import cv2 as cv
#age model
#model structure: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/age.prototxt
#pre-trained weights: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/dex_chalearn_iccv2015.caffemodel
age_model = cv.dnn.readNetFromCaffe("age.prototxt", "dex_chalearn_iccv2015.caffemodel")
 
#gender model
#model structure: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.prototxt
#pre-trained weights: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/static/gender.caffemodel
gender_model = cv.dnn.readNetFromCaffe("gender.prototxt", "gender.caffemodel")
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
    for x, y, w, h in faces_rect:
        detected_face = img[int(y):int(y+h), int(x):int(x+w)]
    detected_face = cv2.resize(detected_face, (224, 224)) #img shape is (224, 224, 3) now
    img_blob = cv2.dnn.blobFromImage(detected_face ) # img_blob shape is (1, 3, 224, 224)   
    cv.imshow('detected faces',frame)
    age_model.setInput(img_blob)
    age_dist = age_model.forward()[0]
    
    gender_model.setInput(img_blob)
    gender_class = gender_model.forward()[0]
    output_indexes = np.array([i for i in range(0, 101)])
    apparent_predictions = round(np.sum(age_dist * output_indexes), 2)  
    gender = 'Woman ' if np.argmax(gender_class) == 0 else 'Man'
    # Display the resulting frame
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
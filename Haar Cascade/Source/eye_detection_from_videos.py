
import numpy as np
import cv2


cap=cv2.VideoCapture('C:\\Users\\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\Data\\eye.mp4')

face_cascade_classifier=cv2.CascadeClassifier('C:\\Users\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\HaarCascadeFiles\\frontalface.xml')
eye_cascade_classifier=cv2.CascadeClassifier('C:\\Users\\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\HaarCascadeFiles\\eye.xml')

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(480,360))

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade_classifier.detectMultiScale(gray_frame,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,70,80),3)

    roi_frame=frame[y:y+h,x:x+w]
    roi_frame_gray=gray_frame[y:y+h,x:x+w]

    eyes=eye_cascade_classifier.detectMultiScale(roi_frame_gray)

    for (xe,ye,we,he) in eyes:
        cv2.rectangle(roi_frame,(xe,ye),(xe+we,ye+he),(0,0,255),3)

    cv2.imshow("frame",frame)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()


    
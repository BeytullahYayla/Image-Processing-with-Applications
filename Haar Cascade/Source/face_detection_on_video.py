import cv2 
import numpy as np

def preprocesss_img(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img



cap=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier("HaarCascadeFiles\\frontalface.xml")



while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    preprocessed_frame=preprocesss_img(frame)
    faces=cascade.detectMultiScale(preprocessed_frame,1.3,2)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Faces",frame)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

import numpy as np
import cv2


face_image=cv2.imread('C:\\Users\\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\Data\\face.png')

face_cascade_classifier=cv2.CascadeClassifier('C:\\Users\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\HaarCascadeFiles\\frontalface.xml')
eye_cascade_classifier=cv2.CascadeClassifier('C:\\Users\\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Haar Cascade\\HaarCascadeFiles\\eye.xml')

gray=cv2.cvtColor(face_image,cv2.COLOR_BGR2GRAY)
faces=face_cascade_classifier.detectMultiScale(gray,1.3,5)
for (x,y,h,w) in faces:
    cv2.rectangle(face_image,(x,y),(x+w,y+h),(0,255,0),2)


#Cropping detected face
face_image2=face_image[y:y+h,x:x+w]
gray2=gray[y:y+h,x:x+h]

eyes=eye_cascade_classifier.detectMultiScale(gray2,1.3,5)

for (xe,ye,he,we) in eyes:
    cv2.rectangle(face_image2,(xe,ye),(xe+we,ye+he),(255,0,0),2)


cv2.imshow("detected image",face_image)
cv2.waitKey(0)
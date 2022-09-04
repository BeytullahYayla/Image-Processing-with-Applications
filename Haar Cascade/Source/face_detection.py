"""
Haar Cascade General Algorithm
1.Import related libraries, image and cascade file
2.Convert rgb image to grayscale image
3.Mark found object(Draw rectangle, circle etc..)


"""
import cv2 
import numpy as np



img=cv2.imread("Data\\face.png")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cascade=cv2.CascadeClassifier("HaarCascadeFiles\\frontalface.xml")

faces=cascade.detectMultiScale(gray_img,1.3,7)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
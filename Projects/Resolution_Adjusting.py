from tkinter import Frame
import cv2
import numpy as np

winodwName="Live Video"
cv2.namedWindow(winname=winodwName)

cap=cv2.VideoCapture(0)

print("Width: "+str(cap.get(3)))
print("Height: "+str(cap.get(4)))


cap.set(3,1280)
cap.set(4,720)
print("Width*: "+str(cap.get(3)))
print("Height*: "+str(cap.get(4)))

while True:
    _,frame=cap.read()

    cv2.imshow(winodwName,frame)


    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
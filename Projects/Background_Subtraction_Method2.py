import cv2 
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\Beytullah\\Downloads\\car.mp4")
subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=100,detectShadows=False)

while True:
    _,frame=cap.read()

    frame=cv2.resize(frame,(640,480))

    mask=subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
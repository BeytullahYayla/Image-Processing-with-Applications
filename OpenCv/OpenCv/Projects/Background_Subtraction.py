import cv2
import numpy as np


cap=cv2.VideoCapture("C:\\Users\\Beytullah\\Downloads\\car.mp4")
ret,first_frame=cap.read()
first_frame=cv2.resize(first_frame,(640,480))
first_frame_gray=cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)
first_frame_blurred=cv2.GaussianBlur(first_frame_gray,(5,5),1)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_blurred=cv2.GaussianBlur(frame_gray,(5,5),1)
    diff=cv2.absdiff(frame_blurred,first_frame_blurred)
    _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    cv2.imshow("Diff",diff)
    if ret==0:
        break
    if cv2.waitKey(30) & 0xFF==ord("q"):
        break



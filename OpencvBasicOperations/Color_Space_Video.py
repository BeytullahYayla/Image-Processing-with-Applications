import cv2
import numpy as np

cap=cv2.VideoCapture("Data\\antalya.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if(ret==0):
        break
    cv2.imshow("Video",frame)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

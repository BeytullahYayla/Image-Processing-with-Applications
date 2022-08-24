import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\Beytullah\\Downloads\\dog.mp4")

while True:
    ret,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    sensivity=15
    
    lower_white=np.array([0,0,255-sensivity])
    upper_white=np.array([255,sensivity,255])

    mask=cv2.inRange(hsv,lower_white,upper_white)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    cv2.imshow("result",res)

    if ret==0:
        break
    #You can access 


    if cv2.waitKey(30) & 0xFF==ord("q"):
        break


cap.release()

cv2.destroyAllWindows()
import cv2 
import numpy as np


cap=cv2.VideoCapture(0)

def preprocess(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    return img

def nothing(x):
    pass
def createTrackbar():
    cv2.namedWindow("Settings")
    cv2.createTrackbar("Lower_Hue","Settings",0,179,nothing)
    cv2.createTrackbar("Lower_Saturation","Settings",0,255,nothing)
    cv2.createTrackbar("Lower_Value","Settings",0,255,nothing)
    cv2.createTrackbar("Upper_Hue","Settings",0,179,nothing)
    cv2.createTrackbar("Upper_Saturation","Settings",0,255,nothing)
    cv2.createTrackbar("Upper_Value","Settings",0,255,nothing)
    
def getTrackbarPositions():
    lh=cv2.getTrackbarPos("Lower_Hue","Settings")
    ls=cv2.getTrackbarPos("Lower_Hue","Settings")
    lv=cv2.getTrackbarPos("Lower_Hue","Settings")
    uh=cv2.getTrackbarPos("Upper_Hue","Settings")
    us=cv2.getTrackbarPos("Upper_Saturation","Settings")
    uv=cv2.getTrackbarPos("Upper_Hue","Settings")

    return (lh,ls,lv,uh,us,uv)
createTrackbar()

while True:

    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.flip(frame,1)
    
    cv2.imshow("Frame",frame)
    frame=preprocess(frame)
    lh,ls,lv,uh,us,uv=getTrackbarPositions()
    lower_blue=np.array([lh,ls,lv])
    upper_blue=np.array([uh,us,uv])

    mask=cv2.inRange(frame,lower_blue,upper_blue)
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("mask",bitwise)

    if(ret==0):
        break

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
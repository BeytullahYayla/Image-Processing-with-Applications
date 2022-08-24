import numpy as np
import cv2

cap=cv2.VideoCapture("C:\\Users\\Beytullah\\Downloads\\eye_motion.mp4")

def preprocess(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,threshold=cv2.threshold(img,2,255,cv2.THRESH_BINARY_INV)
    return threshold

while True:
    ret,frame=cap.read()

    if ret==0:
        break
    
    roi=frame[80:210,230:450]
    rows,cols,cha=roi.shape
    gray=preprocess(roi)
    contours,_=cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    
    for contour in sorted_contours:
        x,y,w,h=cv2.boundingRect(contour)
        
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break
    frame[80:210,230:450]=roi
    cv2.imshow("roi",frame) 


    if cv2.waitKey(30) & 0xFF==ord("q"):
        break
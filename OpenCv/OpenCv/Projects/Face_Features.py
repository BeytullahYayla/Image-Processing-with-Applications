import numpy as np
import cv2 
import math
cap=cv2.VideoCapture(0)

def findMaxContour(contours):
    max_i=0
    max_area=0

    for i in range(len(contours)):
        area_face=cv2.contourArea(contours[i])
        if max_area<area_face:
            max_area=area_face
            max_i=i

        try:
            c=contours[max_i]

        except:
            contours=[0]
            c=contours[0]
        return c

while True:
    ret,frame=cap.read()
    cv2.flip(frame,1)
    roi=frame[50:250,200:400]#frame[y1:y2,x1:x2]

    cv2.rectangle(frame,(250,50),(400,250),(0,0,255),0)

    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    lower_color=np.array([0,45,79],dtype=np.uint8)
    upper_color=np.array([17,255,255],dtype=np.uint8)

    kernel=np.ones((3,3),np.uint8)
    mask=cv2.inRange(hsv,lower_color,upper_color)
    mask=cv2.dilate(mask,kernel,iterations=1)
    mask=cv2.medianBlur(mask,15)

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contours)>0:
        
            c=findMaxContour(contours)

            extLeft=tuple(c[c[:,:,0].argmin()][0])
            extRight=tuple(c[c[:,:,0].argmax()][0])
            extTop=tuple(c[c[:,:,1].argmin()][0])
            extBottom=tuple(c[c[:,:,1].argmax()][0])

            cv2.circle(roi,extLeft,5,(0,255,0),2)
            cv2.circle(roi,extRight,5,(0,255,0),2)
            cv2.circle(roi,extTop,5,(0,255,0),2)
            cv2.circle(roi,extBottom,5,(0,255,0),2)

            cv2.line(roi,extTop,extRight,(255,0,0),2)
            cv2.line(roi,extRight,extBottom,(255,0,0),2)
            cv2.line(roi,extBottom,extLeft,(255,0,0),2)
            cv2.line(roi,extLeft,extTop,(255,0,0),2)

            a = math.sqrt((extRight[0]-extTop[0])**2+(extRight[1]-extTop[1])**2)
            b = math.sqrt((extBottom[0]-extRight[0])**2+(extBottom[1]-extRight[1])**2)
            c = math.sqrt((extBottom[0]-extTop[0])**2+(extBottom[1]-extTop[1])**2)

            try:
                angle_ab=int(math.acos((a**2+b**2-c**2)/(2*b*c))*57)
                cv2.putText(roi,str(angle_ab),(extRight[0]-50,extRight[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),1)

            except:
                cv2.putText(roi,"?",(extRight[0]-50,extRight[1]),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),1)

    


    cv2.imshow("imshow",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("roi",roi)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
from turtle import width
import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\Beytullah\\Downloads\\line.mp4")

def img_preprocess(img):
    img_to_preprocess=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#We want to detect yellow lines on the road. So we need to convert ourcolor space Bgr to HSV color space.
    #img_to_preprocess=cv2.Canny(img_to_preprocess,75,150)
    return img_to_preprocess
    
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    prep_frame=img_preprocess(frame)#Image preprocessed first
    lower_yellow=np.array([18,94,140],np.uint8)
    upper_yellow=np.array([48,255,255],np.uint8)

    mask=cv2.inRange(prep_frame,lower_yellow,upper_yellow)
    edges=cv2.Canny(mask,75,250)

    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=25)

    for line in lines:
        (x1,y1,x2,y2)=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),5)
    cv2.imshow("Masked",mask)
    cv2.imshow("Edges",edges)

    if ret==0:
        break

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

    cv2.imshow("Road",frame)

cap.release()
cv2.destroyAllWindows()

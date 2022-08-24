import cv2
import numpy as np

def nothing(x):
    pass

canvas=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("Canvas")

cv2.createTrackbar("R","Canvas",0,255,nothing)
cv2.createTrackbar("G","Canvas",0,255,nothing)
cv2.createTrackbar("B","Canvas",0,255,nothing)

switch="0: Off, 1: On"
cv2.createTrackbar(switch,"Canvas",0,1,nothing)

while True:
    cv2.imshow("Canvas",canvas)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break


    r=cv2.getTrackbarPos("R","Canvas")
    g=cv2.getTrackbarPos("G","Canvas")
    b=cv2.getTrackbarPos("B","Canvas")
    s=cv2.getTrackbarPos(switch,"Canvas")

    if s==0:
        canvas[:]=[0,0,0]

    if s==1:
        canvas[:]=[b,g,r]
    

cv2.destroyAllWindows()


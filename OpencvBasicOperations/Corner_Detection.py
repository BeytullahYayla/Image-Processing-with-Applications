import cv2
import numpy as np


img=cv2.imread("Data\\contour.png")
img1=cv2.imread("Data\\text.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_text=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)

corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)

corners_text=cv2.goodFeaturesToTrack(gray_text,50,0.01,10)
corners=np.int0(corners)
corners_text=np.int0(corners_text)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)
for corner in corners_text:
    x,y=corner.ravel()
    cv2.circle(img1,(x,y),3,(255,255,0),-1)

cv2.imshow("corner",img)
cv2.imshow("corner2",img1)
cv2.waitKey(0)
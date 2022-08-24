from ctypes import pointer
import cv2 
import numpy as np

img=cv2.imread("Data\\star.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(img_gray,127,255,0)

contours,_=cv2.findContours(thresh,2,1)

cnt=contours[0]
hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    start_point,end_point,far_point,distance=defects[i,0]
    start=tuple(cnt[start_point][0])
    end=tuple(cnt[end_point][0])
    far=tuple(cnt[far_point][0])
    
    cv2.line(img,start,end,(0,255,0),2)
    cv2.circle(img,far,5,[0,255,0],-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
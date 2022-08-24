import cv2
from cv2 import threshold
import numpy as np

img=cv2.imread("Data\\contour1.png")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)


contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img,contours,-1,(0,0,255),3)

cv2.imshow("Image with contours",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
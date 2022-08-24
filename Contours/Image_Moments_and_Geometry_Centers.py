import imghdr
import cv2 
import numpy as np

img=cv2.imread("Data\\contour (1).png")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshold=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)

Movements=cv2.moments(threshold)
X=int(Movements["m10"]/Movements["m00"])
Y=int(Movements["m01"]/Movements["m00"])

circle=cv2.circle(img,(X,Y),5,(0,0,0),thickness=-1)

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(Movements)
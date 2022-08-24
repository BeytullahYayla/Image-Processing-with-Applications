import cv2
from cv2 import threshold
img=cv2.imread("Data\\contour (1).png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)


contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt=contours[0]
area=cv2.contourArea(cnt)#the area of triangle
print(area)
M=cv2.moments(cnt)
print(M["m00"])


perimeter=cv2.arcLength(cnt,True)#The perimeter of triangle
print(perimeter)
cv2.imshow("IMG",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
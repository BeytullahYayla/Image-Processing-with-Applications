import cv2 
import numpy as np

img=cv2.imread("Data\\h_line.png")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny_img=cv2.Canny(gray_img,75,150)


lines=cv2.HoughLinesP(canny_img,1,np.pi/180,50,maxLineGap=200)

print(lines)
for line in lines :
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("Hough Line Orig",img)
cv2.imshow("Canny image",canny_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
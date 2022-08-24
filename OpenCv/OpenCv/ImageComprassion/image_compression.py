import numpy as np
import cv2 

path1="\\Data\\aircraft.jpg"
path2="\\Data\\aircraft.jpg"


img1=cv2.imread(path1)
img1=cv2.resize(img1,(640,550))

img2=cv2.imread(path2)
img2=cv2.resize(img2,(640,550))

if img1.shape==img2.shape:
    print("same size")

diff=cv2.subtract(img1,img2)
b,g,r=cv2.split(diff)

if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
    print("Completely Equal")
else:
    print("Not completely equal")

img3=cv2.medianBlur(img1)
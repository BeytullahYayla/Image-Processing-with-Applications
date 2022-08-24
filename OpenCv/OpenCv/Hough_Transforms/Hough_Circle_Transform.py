from turtle import circle
import cv2
import numpy as np

img1=cv2.imread("C:\\Users\\Beytullah\\Documents\\GitHub\\Deep-Learning-Fundamentals\\OpenCv\\OpenCv\\Data\\coins.jpg")
img2=cv2.imread("C:\\Users\\Beytullah\\Documents\\GitHub\\Deep-Learning-Fundamentals\\OpenCv\\OpenCv\\Data\\balls.jpg")

def preprocess_image(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=cv2.medianBlur(img,5)
    return img

img1_preprocessed=preprocess_image(img1)
img2_preprocessed=preprocess_image(img2)

circles=cv2.HoughCircles(img1_preprocessed,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=40,maxRadius=80)
circles2=cv2.HoughCircles(img2_preprocessed,cv2.HOUGH_GRADIENT,1,img2.shape[0]/16,param1=200,param2=10,minRadius=5,maxRadius=80)
#param1 && param2=>gradient value

print(circles)
if circles is not None:
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img1,(i[0],i[1]),i[2],(0,255,0),3)
    
if circles2 is not None:
    circles2=np.uint16(np.around(circles2))
    for i in circles2[0,:]:
        cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),3)


cv2.imshow("Img1",img1)
cv2.imshow("Img2",img2)
cv2.waitKey(0)
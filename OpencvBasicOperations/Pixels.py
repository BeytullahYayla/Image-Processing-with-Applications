import cv2
import greenlet
import numpy as np

img=cv2.imread("C:\\Users\\Beytullah\\Documents\\GitHub\\Deep-Learning-Fundamentals\\OpenCv\\OpenCv\\Data\\klon.jpg")
dimension=img.shape

print(dimension)
color=img[420,500]#The color of pixel 420,500 is [158 153 144]
print("BGR:",color)

blue=img[420,500][0]
print("Blue:",blue)

green=img[420,500][1]
print("Green:",green)

green=img[420,500][2]
print("Green:",green)

img[420,500][0]=250
print("New Blue",
img[420,500][0])

cv2.imshow("Image",img)
cv2.waitKey(0)
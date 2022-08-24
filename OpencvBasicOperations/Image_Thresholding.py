from pickletools import uint8
import cv2
from cv2 import threshold
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('Data\klon.jpg',0)#Grayscale
cv2.imshow("Img",img)

ret,threshold1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)

cv2.imshow("Returned",ret)
cv2.imshow("Threshold1",threshold1)
cv2.imshow("Threshold3",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
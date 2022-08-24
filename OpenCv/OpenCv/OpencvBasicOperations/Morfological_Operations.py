import cv2
import numpy as np


img=cv2.imread("DATA\\klon.jpg")
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(img,kernel,iterations=1)

dilated=cv2.dilate(img,kernel,iterations=5)

opened=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel=kernel)

cv2.imshow("dilated",dilated)

cv2.imshow("opened",opened)
cv2.imshow("img",img)
cv2.imshow("gradient",gradient)
cv2.imshow("blackhat",blackhat)

cv2.waitKey(0)
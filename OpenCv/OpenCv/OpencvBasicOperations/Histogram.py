import cv2
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((500,500),np.uint8)+50
img2=cv2.imread("Data\\klon.jpg")

cv2.rectangle(img,(0,60),(200,150),(255,255,255),-1)
cv2.rectangle(img,(250,170),(350,200),(255,255,255),-1)
cv2.imshow("img",img)
plt.hist(img.ravel(),255,[0,256])
plt.hist(img2.ravel(),255,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
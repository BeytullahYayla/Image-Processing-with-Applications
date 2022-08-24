import cv2
import numpy as np

#ROI---->Region Of Interest

img=cv2.imread("C:\\Users\\Beytullah\\Documents\\GitHub\\Deep-Learning-Fundamentals\\OpenCv\\OpenCv\\Data\\klon.jpg")
print(img.shape)

roi=img[30:200,200:400]
cv2.imshow("Klon",img)
cv2.imshow("Roi_Klon",roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
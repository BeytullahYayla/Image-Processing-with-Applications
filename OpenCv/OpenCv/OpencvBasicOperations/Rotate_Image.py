import cv2
import numpy as np

img=cv2.imread("Data\\klon.jpg")
row,col,channel=img.shape

transform_matrix=cv2.getRotationMatrix2D((col/2,row/2),90,3)
dst=cv2.warpAffine(img,transform_matrix,(row,col))

cv2.imshow("Rotated Image",dst)
cv2.waitKey(0)

cv2.destroyAllWindows()
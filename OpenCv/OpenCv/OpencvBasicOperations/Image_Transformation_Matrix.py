import cv2
import numpy as np

img=cv2.imread('Data\klon.jpg')
row,col=img.shape

transfrom_matrix=np.float32([1,0,10],[0,1,70])

dst=cv2.warpAffine(img,transfrom_matrix,(row,col))
cv2.imshow('dst',dst)
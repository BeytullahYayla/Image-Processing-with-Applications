import cv2
import numpy as np

img_filter = cv2.imread("D:\\OpenCV\\test_images\\filter.png")
img_median = cv2.imread("D:\\OpenCV\\test_images\\median.png")
img_bilateral = cv2.imread("D:\\OpenCV\\test_images\\bilateral.png")

blur =cv2.blur(img_filter,(5,5))
blur_g=cv2.GaussianBlur(img_filter,(5,5),cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median,5)
blur_b = cv2.bilateralFilter(img_bilateral,9,95,95)

cv2.imshow("original",img_bilateral)
cv2.imshow("blur_b",blur_b)


cv2.waitKey(0)
cv2.destroyAllWindows()

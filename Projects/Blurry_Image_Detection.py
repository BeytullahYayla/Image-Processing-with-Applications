import cv2 
import numpy as np

img=cv2.imread("Data\\starwars.jpg")
blurry_img=cv2.medianBlur(img,7)

laplacian=cv2.Laplacian(blurry_img,cv2.CV_64F).var()

if laplacian<500:
    print("Image is blurry")

else :
    print("Image is not blurry")

print(laplacian)

cv2.imshow("original image",img)

cv2.imshow("blurry image",blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
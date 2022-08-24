import cv2

img=cv2.imread("klon1.jpg",cv2.WINDOW_NORMAL)
img=cv2.resize(img,(640,480))
cv2.imshow("Resized Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2 
import numpy as np

#f(x,y)=x*a+y*b+c

circle=np.zeros((512,512,3),np.uint8)+255
cv2.circle(circle,center=(256,256),radius=60,color=(255,0,0),thickness=-1)

rectangle=np.zeros((512,512,3),dtype=np.uint8)+255
cv2.rectangle(rectangle,(150,150),(350,350),color=(0,0,255),thickness=-1)

dst=cv2.addWeighted(circle,0.3,rectangle,0.7,0)
cv2.imshow("Dst",dst)

cv2.imshow("Circle",circle)
cv2.imshow("Rectangle",rectangle)

add=cv2.add(circle,rectangle)
cv2.imshow("Added Image",add)
print(add[256,256])
cv2.waitKey(0)

cv2.destroyAllWindows()
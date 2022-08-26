import cv2 
import numpy as np

image="Data\\starwars (1).jpg"
template_path="Data\\starwars2.jpg"

img=cv2.imread(image)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

template=cv2.imread(template_path,0)

w,h=template.shape[::-1]
result=cv2.matchTemplate(gray_img,template,cv2.TM_CCOEFF_NORMED)

location=np.where(result>=0.9)

for point in zip(*location[::-1]):
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),1)



cv2.imshow("template",template)
cv2.imshow("result",result)
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
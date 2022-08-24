
import cv2 
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX#Font
font1=cv2.FONT_HERSHEY_COMPLEX

img=cv2.imread("Data\\polygons.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold=cv2.threshold(img_gray,240,255,cv2.THRESH_BINARY)



contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(contours)
for cnt in contours:

    epsilon=0.01*cv2.arcLength(cnt,True)
    approx=cv2.approxPolyDP(cnt,epsilon,True)
    cv2.drawContours(img,[approx],0,(0),5)

    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y),font,1,(0))
    
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y),font,1,(0))
    
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),font,1,(0))
    
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),font,1,(0))

    else:
        cv2.putText(img,"Ellipse",(x,y),font,1,(0))


    

cv2.imshow("Polygons",img)


cv2.waitKey(0)
cv2.destroyAllWindows()
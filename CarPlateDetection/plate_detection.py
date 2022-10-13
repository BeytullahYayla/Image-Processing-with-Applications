import cv2 
import numpy as np
import imutils
import pytesseract

#bilateral_filter=A bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter for images. It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels.
#canny=The Canny edge detector is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images. 
#find_countours

#After we cropped to image we can read text in the plate using pyteserract

img=cv2.imread('C:\\Users\\Beytullah\\Documents\\GitHub\\Image-Processing-with-Applications\\Data\\licence_plate (2).jpg')
print(type(img))#returns a numpy array
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
smoothened_img=cv2.bilateralFilter(gray,5,250,250)
edged=cv2.Canny(smoothened_img,30,200)

contours=cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnts=imutils.grab_contours(contours)

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]

screen=None
#arcLenght finds length of arcs 
for cnt in cnts:
    epsilon=0.018*cv2.arcLength(cnt,True)
    approx=epsilon*cv2.approxPolyDP(cnt,epsilon,True)#This method is getting closer to contours each other
    if len(approx)==4:
        screen=approx
        print(screen)
        break

mask=np.zeros(shape=gray.shape,dtype=np.uint8)
new_image,hierarchy=cv2.drawContours(mask,contours=screen,contourIdx=0,color=(255,255,255),thickness=-1)
new_image=cv2.bitwise_and(img,img,mask)#It pastes img to mask field


(x,y)=np.where(mask==255)
(x_top,y_top)=(np.min(x),np.min(y))
(x_bottom,y_bottom)=(np.max(x),np.max(y))
cropped=gray[x_top:x_bottom+1,y_top:y_bottom+1]



text=pytesseract.image_to_string(cropped,lang="eng")
print("Detected Text",text)

cv2.imshow("cropped",cropped)


cv2.waitKey(0)
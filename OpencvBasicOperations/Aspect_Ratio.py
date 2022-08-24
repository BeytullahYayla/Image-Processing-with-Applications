import cv2

def resizeWithAspectRatio(img,width=None,height=None,inter=cv2.INTER_AREA):
    dimension=None
    (h,w)=img.shape[:2]

    if width is None and height is None:
        return img
    
    if width is None:
        r=height/float(h)
        dimension=(int(w*r),height)
    else:
         r=width/float(w)
         dimension=(width,int(h*r))

    return cv2.resize(img,dimension,interpolation=inter)

img=cv2.imread("Data/klon.jpg")
cv2.imshow("Original Image",img)
img=resizeWithAspectRatio(img,200)
cv2.imshow("ResizedWithAspectRatio",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
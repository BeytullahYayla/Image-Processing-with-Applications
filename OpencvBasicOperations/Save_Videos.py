import cv2
cap=cv2.VideoCapture(0)

filename="C:\\Users\\Beytullah\\Desktop\\Python\\Videos\\webcam.avi"
codec=cv2.VideoWriter_fourcc('W','M','V','2')
frame_rate=30
resolution=(640,480)
videoFileOutput=cv2.VideoWriter(filename,codec,frame_rate,resolution)

while True:
    ret,frame=cap.read()

    if ret==0:
        break

    frame=cv2.flip(frame,1)#Flips by y axis
    videoFileOutput.write(frame)
    cv2.imshow("Webcam Live",frame)

    if cv2.waitKey(30) & 0xFF==ord("q"):
        break

cv2.relase()
cv2.destroyAllWindows()

import cv2
import numpy as np
def apply_filter(img,f):
    if f =="r": img[:,:,1]=img[:,:,0]=0
    elif f =="g": img[:,:,0]=img[:,:,2]=0
    elif f =="b": img[:,:,1]=img[:,:,2]=0
    elif f =="s":
        g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(cv2.Sobel(g,cv2.CV_8U,1,1,3),cv2.COLOR_GRAY2BGR)
    elif f =="c":
        g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img=cv2.cvtColor(cv2.Canny(g,100,200),cv2.COLOR_GRAY2BGR)
    elif f =="t":
        g=cv2.medianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),5)
        e=cv2.adaptiveThreshold(g,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
        img = cv2.bitwise_and(cv2.bilateralFilter(img,9,300,300),cv2.bilateralFilter(img,9,300,300),mask=e)
    return img
cap=cv2.VideoCapture(0)
f= None
print("r,g,b,s,c,t filter | q quit")
while cap.isOpened():
    ret,frame =cap.read()
    if not ret : break
    out=apply_filter(frame.copy(),f) if f else frame
    cv2.imshow("Filters",out)
    k=cv2.waitKey(1) & 0xFF
    if k in [ord(x) for x in "rgb sct"]: f=chr(k)
    elif k== ord('q'):break
cap.release()
cv2.destroyAllWindows()

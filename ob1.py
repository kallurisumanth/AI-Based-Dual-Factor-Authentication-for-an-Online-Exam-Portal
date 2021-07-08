import cv2
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string
path='haarcascades/haarcascade_mobile.xml' #path
cameraNo=1                  #camera number
objectName='Mobile'           #object name to display
frameWidth=640              #display width
frameHeight=480             #display height
color=(255,0,255)

cap=cv2.VideoCapture(cameraNo)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass

#create trackbar
cv2.resizeWindow("Result",frameWidth,frameHeight+100)
cv2.createTrackbar("Scale","Result",400,1000,empty)
cv2.createTrackbar("Neig","Result",8,20,empty)
cv2.createTrackbar("Min Area","Result",0,100000,empty)
cv2.createTrackbar("Brightness","Result",180,255,empty)

#load the classifiers downloaded
cascade=cv2.CascadeClassifier(path)

while True:
    #set camera brightness from trackbar value
    cameraBrightness=cv2.getTrackbarPos("Brightness","Result")
    cap.set(10,cameraBrightness)
    #get camera image and convert to grayscale
    success, img=cap.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detect the object using the cascade
    scaleVal=1+(cv2.getTrackbarPos("Scale","Result")/1000)
    neig=cv2.getTrackbarPos("Neig","Result")
    objects=cascade.detectMultiScale(gray,scaleVal,neig)

    #display the detected objects
    for(x,y,w,h) in objects:
        area=w*h
        minArea=cv2.getTrackbarPos("Min Area","Result")
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
            cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            roi_color=img[y:y+h,x:x+w]

    cv2.imshow("Result",img)
    if cv2.waitkey(1) & 0xFF ==ord('q'):
        break

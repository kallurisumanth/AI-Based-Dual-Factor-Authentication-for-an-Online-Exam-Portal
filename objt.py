import cv2
import os
import time

myPath='data/images'
cameraNo=1
cameraBrightness=190
moduleval=10
grayImage=False
saveData=True
showImage=True
imgWidth=180
imgHeight=120

global countFolder
cap=cv2.VideoCapture(cameraNo)
cap.set(3,640)
cap.set(4,480)
cap.set(10,cameraBrightness)

count=0
countsave=0

def saveDataFunc():
    global countFolder
    countFolder=0
    while os.path.exists( myPath+str(countFolder)):
        countFolder=countFolder+1
    os.makedirs(myPath+str(countFolder))

if saveData:saveDataFunc()

while True:
    success,img=cap.read()
    img=cv2.resize(img,(imgWidth,imgHeight))
    if grayImage:img=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
    if saveData:
        blur=cv2.Laplacian(img,cv2.CV_64F).var()
        if count%moduleval==0 and blur>minBlur:
            nowTime=time.time()
            cv2.imwrite(myPath+str(countFolder)+'/'+str(countsave)+"_"+str(int(blur))+"_"+str(nowTime)+".png",img)
        count+=1
    if showImage:
        cv2.imshow("Image",img)
    if cv2.waitkey(1) & oxFF==ord('q'):
        break
cap.release()
cv2.destroyAllwindows()
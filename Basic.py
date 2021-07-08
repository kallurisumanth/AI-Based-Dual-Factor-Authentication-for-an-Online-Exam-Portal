import cv2
import numpy as np
import face_recognition
import os

path='Imagesdatabse'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
print(images)
def findEncodings(images):
    encodeList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
encodeListKnown=findEncodings(images)
#print(len(encodeListKnown))
print("Encoding complete")
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
cap=face_recognition.load_image_file('opencv_frame.png')
cap=cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
known=[]
while True:
   # success,img=cap.read()
   # imgS=cv2.resize(img,(0,0),None,0.25,0.25)
   # imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facesCurFrame=face_recognition.face_locations(cap)
    encodesCurrFrame=face_recognition.face_encodings(cap,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurrFrame,facesCurFrame):
        matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnown,encodeFace)
        print(faceDis)
        matchIndex=np.argmin(faceDis)
        if matches[matchIndex]:
            name=classNames[matchIndex].upper()
            known.append(name)
    break
if len(known)==0:
    print("no match found")
else:
    print(known[0])

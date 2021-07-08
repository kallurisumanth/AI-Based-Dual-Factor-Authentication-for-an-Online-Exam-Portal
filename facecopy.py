import cv2
import numpy as np
import face_recognition
import os
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class RegisterFace:
    def __init__(self,root):
        self.root=root
        self.root.title("Face Authentication")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")
        #bg image
       # self.bg=ImageTk.PhotoImage(file="images/14.jpeg")
        #bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        # left image
        self.left = ImageTk.PhotoImage(file="images/15.png")
        left = Label(self.root, image=self.left,bg="orange").place(x=0, y=85, width=540, height=400)
        #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=40,width=800,height=630)
        title=Label(frame1,text="Face authentication", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        #----row1
        userid = Label(frame1, text="User ID", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=90)
        self.txt_userid = Entry(frame1, font=("times new roman", 15), bg="lightgray", )
        self.txt_userid.place(x=50, y=120, width=250)

        btn_register = Button(frame1, text="Open Cam", command=self.open_cam, font=("times new roman", 20),
                              bg="#009dc4", bd=0, cursor="hand2").place(x=390, y=520, width=180, height=50)
    def open_cam(self):
        path = 'Imagesdatabse'
        images = []
        classNames = []
        myList = os.listdir(path)
        print(myList)
        for cl in myList:
            classNames.append(os.path.splitext(cl)[0])
        print(classNames)
        if self.txt_userid.get() in classNames:
            imgElon = face_recognition.load_image_file('Imagesdatabse/'+self.txt_userid.get()+'.jpg')
            imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
            facesCurFrame = face_recognition.face_locations(imgElon)
         #   cv2.imshow('Elon Musk', imgElon)
         #   cv2.waitKey(0)
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
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = "opencv_frame.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    img_counter += 1
                    messagebox.showinfo("Success", "Picture Captured Successfully", parent=self.root)
                    break

            cam.release()
            cv2.destroyAllWindows()
            imgTest = face_recognition.load_image_file('opencv_frame.png')
            imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

            facesCurFrame1 = face_recognition.face_locations(imgTest)

            if len(facesCurFrame1) == 0:
                messagebox.showerror("Error", "your face is not captured properly", parent=self.root)
            else:
                if len(facesCurFrame) != 0:
                    faceLoc = face_recognition.face_locations(imgElon)[0]
                    encodeElon = face_recognition.face_encodings(imgElon)[0]
                    cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

                    faceLocTest = face_recognition.face_locations(imgTest)[0]
                    encodeTest = face_recognition.face_encodings(imgTest)[0]
                    cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]),
                                  (255, 0, 255), 2)

                    results = face_recognition.compare_faces([encodeElon], encodeTest)
                    print(results)
                    if results:
                        messagebox.showinfo("Success", "Matched successfully", parent=self.root)
                        self.root.destroy()
                    else:
                        messagebox.showerror("Error:", " User not registered", parent=self.root)
        else:
            messagebox.showerror("Error:", " User not registered", parent=self.root)

     #   import admin_login
"""
path='Imagesdatabse'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cl in myList:
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

imgElon = face_recognition.load_image_file('ImagesBasic/sumanth.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/sumanth.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

facesCurFrame = face_recognition.face_locations(imgElon)
facesCurFrame1 = face_recognition.face_locations(imgTest)
if len(facesCurFrame1) == 0:
    print("your face is not captured properly")
else:
    if len(facesCurFrame) != 0:
        faceLoc = face_recognition.face_locations(imgElon)[0]
        encodeElon = face_recognition.face_encodings(imgElon)[0]
        cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

        faceLocTest = face_recognition.face_locations(imgTest)[0]
        encodeTest = face_recognition.face_encodings(imgTest)[0]
        cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

        results = face_recognition.compare_faces([encodeElon], encodeTest)
        print(results)

 #       cv2.imshow('Elon Musk', imgElon)
#      cv2.imshow('Elon Test', imgTest)
#       cv2.waitKey(0)
    else:
        print("no match found")
"""
root=Tk()
obj=RegisterFace(root)
root.mainloop()
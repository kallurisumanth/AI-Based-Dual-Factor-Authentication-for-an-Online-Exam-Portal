from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import os
import cv2
import face_recognition
import cv2
import random
import smtplib
from tkinter import simpledialog
import tkinter as tk

class Hii:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")
        # bg image
        # self.bg=ImageTk.PhotoImage(file="images/14.jpeg")
        # bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        # left image
        self.left = ImageTk.PhotoImage(file="images/15.png")
        left = Label(self.root, image=self.left, bg="orange").place(x=0, y=85, width=540, height=400)
        # register frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=40, width=800, height=630)
        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=50, y=30)
        # ----row1

        f_name = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=90)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray", )
        self.txt_fname.place(x=50, y=120, width=250)

        l_name = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=90)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=120, width=250)
        # -----row2
        userid = Label(frame1, text="User ID.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=160)
        self.txt_userid = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_userid.place(x=50, y=190, width=250)

        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=370,
                                                                                                               y=160)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=190, width=250)

        # -----row3
        password = Label(frame1, text="Password.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=230)
        self.txt_password = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=280, width=250)

        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                          fg="gray").place(x=370, y=230)
        self.txt_cpassword = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=370, y=280, width=250)
        # new row
        status = Label(frame1, text="status.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=330)
        self.txt_status = ttk.Combobox(frame1, font=("times new roman", 15))
        self.txt_status['values'] = ("select", "Student")
        self.txt_status.place(x=50, y=370, width=250)
        gender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=370, y=330)
        self.cmb_gend = ttk.Combobox(frame1, font=("times new roman", 13))
        self.cmb_gend['values'] = ("select", "Male", "Female")
        self.cmb_gend.place(x=370, y=370, width=250)
        # new row2
        address = Label(frame1, text="Address.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=410)
        self.txt_address = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_address.place(x=50, y=450, width=250, height=60)

        dob = Label(frame1, text="Date Of Birth.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=370, y=410)
        self.txt_dob = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_dob.place(x=370, y=450, width=250)
        # new row
        country = Label(frame1, text="Country.", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(
            x=50, y=520)
        self.txt_country = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_country.place(x=50, y=550, width=250)



        self.btn_img = ImageTk.PhotoImage(file="images/7.jpg")
        btn_register = Button(frame1, text="Register Now", command=self.register_data, font=("times new roman", 20),
                              bg="#009dc4", bd=0, cursor="hand2").place(x=450, y=550, width=180, height=50)
        btn_login = Button(self.root, text="Sign In", command=self.login_window, font=("times new roman", 20),
                           bg="gray", bd=0, cursor="hand2").place(x=250, y=450, width=150)
        btn_login = Button(self.root, text="Admin Sign In", command=self.admin_login_window,
                           font=("times new roman", 20), bg="gray", bd=0, cursor="hand2").place(x=230, y=520, width=200)
        btn_login = Button(self.root, text="Home", command=self.home,
                           font=("times new roman", 20), bg="gray", bd=0, cursor="hand2").place(x=230, y=590, width=200)
    def admin_login_window(self):
        self.root.destroy()
        import adminlogin
    def login_window(self):
        self.root.destroy()
        import studentlogin
    def home(self):
        self.root.destroy()
        import home
    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_userid.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_status.delete(0, END)
        self.cmb_gend.delete(0, END)
        self.txt_country.delete(0, END)
        self.txt_dob.delete(0, END)
        self.txt_address.delete(0, END)
        

    def register_data(self):
        if self.txt_fname.get() == "" and self.txt_lname.get() == "" and self.txt_email.get() == "" and self.txt_userid.get() == "" and self.txt_password.get() == "" and self.txt_cpassword.get() == "" and self.txt_status.get() == "select" and self.txt_address.get() == "" and self.txt_dob.get() == "" and self.txt_country.get() == "" and self.cmb_gend.get() == "select":
            messagebox.showerror("Error:", " All fields are required", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error:", " Password and confirm password should be same", parent=self.root)
        else:
            try:
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
                        img_name = "Imagesdatabse/" + self.txt_userid.get() + ".jpg".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        print("{} written!".format(img_name))
                        img_counter += 1
                        break

                cam.release()

                cv2.destroyAllWindows()
                imgTest = face_recognition.load_image_file("Imagesdatabse/" + self.txt_userid.get() + '.jpg')
                imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
                facesCurFrame1 = face_recognition.face_locations(imgTest)

                if len(facesCurFrame1) == 0:
                    messagebox.showerror("Error", "your face is not captured properly", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Image captured successfully", parent=self.root)
                    messagebox.showinfo("Proceed", "OTP sent to particular email id", parent=self.root)

                    def otp_generation(emailid):
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()

                        password = 'gvdbhqltmavjjiew'
                        server.login('kalyanvanan00@gmail.com', password)

                        otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                        msg = 'Hello, Your OTP is ' + str(otp)
                        sender = 'kalyanvanan00@gmail.com'
                        receiver = emailid

                        server.sendmail(sender, receiver, msg)
                        server.quit()
                        return str(otp)

                    emailid = self.txt_email.get()
                    otp = otp_generation(emailid)
                    application_window = tk.Tk()
                    user_entered_otp = simpledialog.askstring("Input", "Please enter OTP",
                                                    parent=application_window)
                    if otp == user_entered_otp:
                        messagebox.showinfo("Success", "OTP matched successfully", parent=self.root)
                        con = pymysql.connect(host="localhost", user="root", password="sumanth01284469",
                                              database="examapplication")
                        cur = con.cursor()
                        cur.execute("select*from faculty where userid=%s", self.txt_userid.get())
                        row = cur.fetchone()
                        if row != None:
                            messagebox.showerror("Error", "User already existed", parent=self.root)
                        else:
                            cur.execute(
                                "insert into faculty(f_name,l_name,userid,email,password,cpassword,status,gender,address,dob,country) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (
                                    self.txt_fname.get(), self.txt_lname.get(), self.txt_userid.get(),
                                    self.txt_email.get(),
                                    self.txt_password.get(), self.txt_cpassword.get(), self.txt_status.get(),
                                    self.cmb_gend.get(), self.txt_address.get(), self.txt_dob.get(),
                                    self.txt_country.get()
                                ))
                            con.commit()
                            con.close()

                        messagebox.showinfo("Success", "Register Successful", parent=self.root)
                        self.clear()
                    else:
                        messagebox.showerror("Error:", " OTP doesn't matched",
                                             parent=self.root)
                        print("You Entered Wrong OTP")


            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)


root = Tk()
obj = Hii(root)
root.mainloop()
from tkinter import*
from tkinter import ttk,messagebox
from datetime import *
import time
from math import*
from PIL import Image,ImageTk
import pymysql
class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        # Background color
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
        #frames
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="Client Login here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email = Label(login_frame, text="User Name/EMail :", font=("times new roman", 18, "bold"), bg="white",fg="gray").place(x=245, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350,height=35)

        password=Label(login_frame, text="Password :", font=("times new roman", 18, "bold"), bg="white",fg="gray").place(x=245, y=250)
        self.txt_password = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=250, y=280, width=350, height=35)
        btn_reg=Button(login_frame,cursor="hand2",text="Register new account",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        btn_login = Button(self.root, text="Log In",command=self.login, font=("times new roman", 20,"bold"), bg="grey", bd=0,cursor="hand2").place(x=500, y=470, width=180,height=40)

    def register_window(self):
        print("hi8")
    def login(self):
        print("bye9")
root=Tk()
obj=Login_window(root)
root.mainloop()
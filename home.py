from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class Home:
    def __init__(self,root):
        self.root=root
        self.root.title("EXAM PORTAL")
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
        title=Label(frame1,text="EXAM PORTAL", font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        btn_register = Button(frame1, text="Register New", command=self.register_data, font=("times new roman", 20),
                              bg="#009dc4", bd=0, cursor="hand2").place(x=200, y=300, width=180, height=50)
        btn_login = Button(frame1, text="Sign In", command=self.login_window, font=("times new roman", 20),
                           bg="gray", bd=0, cursor="hand2").place(x=220, y=100, width=150)
        btn_login = Button(frame1, text="Admin Sign In", command=self.admin_login_window,
                           font=("times new roman", 20), bg="gray", bd=0, cursor="hand2").place(x=200, y=200, width=200)
    def admin_login_window(self):
        self.root.destroy()
        import adminlogin
    def login_window(self):
        self.root.destroy()
        import studentlogin

    def register_data(self):
        self.root.destroy()
        import register

root=Tk()
obj=Home(root)
root.mainloop()
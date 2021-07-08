from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class exam:
    def __init__(self,root):
        self.root=root
        self.root.title("Exam Portal")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=40, width=800, height=630)
        title = Label(frame1, text="Welcome to exam portal", font=("times new roman", 20, "bold"), bg="white", fg="green").place(
            x=50, y=30)
        btn_login = Button(frame1, text="Home", command=self.gotohome,
                           font=("times new roman", 20), bg="gray", bd=0, cursor="hand2").place(x=200, y=200, width=200)
    def gotohome(self):
        self.root.destroy()
        import home
root=Tk()
obj=exam(root)
root.mainloop()
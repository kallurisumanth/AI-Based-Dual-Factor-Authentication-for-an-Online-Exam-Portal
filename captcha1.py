from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
import random
import string
from captcha.image import ImageCaptcha


class Home:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")

        # bg image
        # self.bg=ImageTk.PhotoImage(file="images/14.jpeg")
        # bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        # left image
        self.left = ImageTk.PhotoImage(file="sam.png")
        left = Label(self.root, image=self.left, bg="orange").place(x=0, y=85, width=540, height=400)
        # register frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=40, width=800, height=630)
        title = Label(frame1, text="CAPTCHA", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50,
                                                                                                                  y=30)
        l_name = Label(frame1, text="Enter the captcha", font=("times new roman", 15, "bold"), bg="white",
                       fg="gray").place(x=300, y=110)
        self.txt_lname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=300, y=140, width=250)
        btn_login = Button(self.root, text="regenerate", command=self.generate_otp, font=("times new roman", 18),
                           bg="gray", bd=0, cursor="hand2").place(x=190, y=350, width=130)
        btn_login1 = Button(frame1, text="Check", command=self.checking, font=("times new roman", 18),
                           bg="gray", bd=0, cursor="hand2").place(x=190, y=350, width=130)
    def admin_login_window(self):
        self.root.destroy()
        import adminlogin
    def generate_otp(self):
        global x
        def generate_random_number(length):
            return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))

        image = ImageCaptcha()
        x = generate_random_number(5)
        data = image.generate(str(x))
        image.write(str(x), 'sam.png')
      #  print(x)
        self.root.destroy()
        import captcha1
    def checking(self):
        global x
        print(x)
        if int(x)==int(self.txt_lname.get()):
            messagebox.showinfo("Success", "Captcha is correct", parent=self.root)
        else:
            messagebox.showerror("Error:", " CAPTCHA IS INCORRECT", parent=self.root)

root = Tk()


def generate_random_number(length):
    return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))


image = ImageCaptcha()
x = generate_random_number(5)
data = image.generate(str(x))
image.write(str(x), 'sam.png')
obj = Home(root)
root.mainloop()
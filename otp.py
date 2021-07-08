import random
import smtplib

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

emailid=input("Enter your email id ")
otp=otp_generation(emailid)
user_entered_otp = input()
if otp == user_entered_otp:
    print("Login Successful")
else:
    print("You Entered Wrong OTP")
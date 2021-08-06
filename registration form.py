
from tkinter import *
import os
import smtplib

root = Tk()

email_string = StringVar(root)

root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Sign Up",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_3 = Entry(root,textvariable=email_string)
entry_3.place(x=240,y=180)
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
label_4 = Label(root, text="Age:",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_2 = Entry(root)
entry_2.place(x=240,y=280)

label_5 = Label(root, text="Password",width=20,font=("bold", 10))
label_5.place(x=70,y=330)
label_6=Label(root, text="Conform Password",width=20,font=("bold", 10))
label_6.place(x=70,y=380)
entry_4=Entry(root,show='*')
entry_4.place(x=240,y=330)
entry_5=Entry(root,show='*')
entry_5.place(x=240,y=380)




def Send_Email(email, password, to, subject, message):

    with smtplib.SMTP('smtp.gmail.com:587') as server:
        server.ehlo()  # local host
        server.starttls()  # Puts the connection to the SMTP server.
        # login to the account of the sender
        server.login(email, password)
        # Format the subject and message together
        message = 'Subject: {}\n\n{}'.format(subject, message)
        # Sends the email from the logined email to the receiver's email
        server.sendmail(email, to, message)
        print('Email sent')

def login():
    root.destroy()
    os.system('py Login_page.py')
    Send_Email('manideepalla0208@gmail.com','ddqllpelnokaeaoc', email_string.get() ,'Thanks for Registering','Thank you for Registering.......')

Button(root, text='Submit',width=20,bg='brown',fg='white',command=login).place(x=180,y=430)
root.mainloop()
print("registration form  seccussfully created...")

from tkinter import *

def pay():
    label_2.config(text='Payment successful...and your slot is booked')

root = Tk()
root.geometry('600x600')
root.title("Otp verification")
label_0 = Label(root, text="An OTP is sent to your mobile.If you didn't recieve click on \"Resend\" option",width=60,font=("bold", 10))
label_0.place(x=40,y=53)
label_1=Label(root,text="OTP:",width=20,font=("bold",10))
label_1.place(x=80,y=130)
entry_1=Entry(root)
entry_1.place(x=240,y=130)
label_2=Label(root,width=60,font=("bold",10))
label_2.place(x=50,y=250)
Button(root,text="submit",width=20,bg='brown',fg='white',command=pay).place(x=100,y=180)
Button(root,text="Resend",width=20,bg='brown',fg='white').place(x=300,y=180)
root.mainloop()

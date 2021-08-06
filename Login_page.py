from tkinter import *
import os

root = Tk()
def main():
    root.destroy()
    os.system("py main_page.py")


root.geometry('800x800')
root.title("Login Page")
label_0 = Label(root, text="Login page",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="Email:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
c
label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2=Entry(root,show='*')
entry_2.place(x=240,y=180)
Button(root, text='Login',width=20,bg='brown',fg='white',command=main).place(x=240,y=230)
root.mainloop()

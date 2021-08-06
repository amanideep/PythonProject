from tkinter import *
from PIL import ImageTk, Image
import os





root = Tk()
var = IntVar(root)

var1 = IntVar(root)
def book():
    root.destroy()
    os.system("py billing_page.py")

def next_page():
    root.destroy()
    os.system("py main_page3.py")


def prev_page():
    root.destroy()
    os.system("py main_page.py")


root.geometry('1500x1500')
img = ImageTk.PhotoImage(Image.open("project_images/football.jpg").resize((400,200), Image.ANTIALIAS))
image = Label(root, image = img).grid(row = 0, column = 0, sticky = W, pady = 20,padx=220)
Label_2=Label(root, text="Foot Ball",width=20,font=("bold", 15)).place(x=400,y=10)
label_0 = Label(root,width=20,font=("bold", 20)).grid(row = 1, column = 0, sticky = W, pady = 20,padx=450)
Button(root,text="Book now",width=20,bg='brown',fg='white',command=book).place(x=1000,y=255)
Label_1 = Label(root,width=20,text="Select Day:",font=("bold",15)).place(x=10,y=230)
rb_1 = Radiobutton(root,text='Monday',variable=var, value=1).place(x=200,y=230)
rb_2 = Radiobutton(root,text='Tuesday',variable=var, value=2).place(x=300,y=230)
rb_3 = Radiobutton(root,text='Wednesday',variable=var, value=3).place(x=400,y=230)
rb_4 = Radiobutton(root,text='Thursday',variable=var, value=4).place(x=500,y=230)
rb_5 = Radiobutton(root,text='Friday',variable=var, value=5).place(x=600,y=230)
rb_6 = Radiobutton(root,text='Saturday',variable=var, value=6).place(x=700,y=230)
rb_7 = Radiobutton(root,text='Sunday',variable=var, value=7).place(x=800,y=230)
Label_1=Label(root, text="Select slot:",width=20,font=("bold", 15)).place(x=10,y=280)
Radiobutton(root,text='6AM-8AM',padx = 5, variable=var1, value=1).place(x=200,y=280)
Radiobutton(root,text='8AM-10AM',padx = 5, variable=var1, value=2).place(x=300,y=280)
Radiobutton(root,text='10AM-12PM',padx = 5, variable=var1, value=3).place(x=400,y=280)
Radiobutton(root,text='3PM-5PM',padx = 5, variable=var1, value=4).place(x=500,y=280)
Radiobutton(root,text='5PM-7PM',padx = 5, variable=var1, value=5).place(x=600,y=280)
Radiobutton(root,text='7PM-9PM',padx = 5, variable=var1, value=6).place(x=700,y=280)
img_2 = ImageTk.PhotoImage(Image.open("project_images/basket.jpeg").resize((400,200), Image.ANTIALIAS))
image_2 = Label(root, image = img_2).grid(row = 5, column = 0, sticky = W, pady = 20,padx=220)
Label_3=Label(root, text="Basket Ball",width=20,font=("bold", 15)).place(x=400,y=320)
Label_1=Label(root, text="Select day:",width=20,font=("bold", 15)).place(x=10,y=630)
rb_1 = Radiobutton(root,text='Monday',variable=var, value=1).place(x=200,y=630)
rb_2 = Radiobutton(root,text='Tuesday',variable=var, value=2).place(x=300,y=630)
rb_3 = Radiobutton(root,text='Wednesday',variable=var, value=3).place(x=400,y=630)
rb_4 = Radiobutton(root,text='Thursday',variable=var, value=4).place(x=500,y=630)
rb_5 = Radiobutton(root,text='Friday',variable=var, value=5).place(x=600,y=630)
rb_6 = Radiobutton(root,text='Saturday',variable=var, value=6).place(x=700,y=630)
rb_7 = Radiobutton(root,text='Sunday',variable=var, value=7).place(x=800,y=630)
Label_2=Label(root, text="Select slot:",width=20,font=("bold", 15)).place(x=10,y=680)
Radiobutton(root,text='6AM-8AM',padx = 5, variable=var1, value=1).place(x=200,y=680)
Radiobutton(root,text='8AM-10AM',padx = 5, variable=var1, value=2).place(x=300,y=680)
Radiobutton(root,text='10AM-12PM',padx = 5, variable=var1, value=3).place(x=400,y=680)
Radiobutton(root,text='3PM-5PM',padx = 5, variable=var1, value=4).place(x=500,y=680)
Radiobutton(root,text='5PM-7PM',padx = 5, variable=var1, value=5).place(x=600,y=680)
Radiobutton(root,text='7PM-9PM',padx = 5, variable=var1, value=6).place(x=700,y=680)
Button(root,text="Book now",width=20,bg='brown',fg='white',command=book).place(x=1000,y=655)
Button(root,text="Next page",width=20,bg='brown',fg='white',command=next_page).place(x=1340,y=755)
Button(root,text="Previous page",width=20,bg='brown',fg='white',command=prev_page).place(x=10,y=755)





root.mainloop()

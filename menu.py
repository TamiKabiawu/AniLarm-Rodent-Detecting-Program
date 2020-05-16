from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#this is just laying out the basics window of the GUI
top = Tk()
top.geometry("500x570")
top.title("Animal Watcher")

#This is used to Style the top of the Window
frame = Frame(top, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
frame.config(background='light blue')
label = Label(frame,text="Animal Watcher", bg='light blue', font=('Times 35 bold'))
label.pack(side=TOP)

#creates a Tkinter iamge that can be used everywhere Tkinter expects an image object
path = "Fall-beautiful-nature.jpg"
img = ImageTk.PhotoImage(Image.open(path))

#This is used to insert the Image
background_label = Label(top, image=img)
background_label.pack(side=TOP)

#this is a sample function called hello
def hello():
    messagebox.showinfo("Say Hello", "Hello World")

#command is the function or method to be called when the button is pressed
B1 = Button(padx=5,pady=5, text = "START WATCHING", font=('helvetica 15 bold'), bg= 'white', fg='black', relief=GROOVE, command=hello)
B1.place(x=165, y=104)


top.mainloop()


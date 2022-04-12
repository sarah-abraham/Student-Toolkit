from tkinter import *
import tkinter as tk


root = Tk()

frame1=Canvas(root,bg = "indigo",bd=10,width=850,height=100)
frame1.place(x=0,y=0)

frame1.create_text(400, 70, text="Student Toolkit", fill="lightsteelblue2", font=('Helvetica 25 bold'))
frame1.pack()
# specify size of window.
root.geometry("850x750+0+0")
root.configure(bg="purple3")

def conv2doc():
    exec(open('pdf2word.py').read())

def conv2pdf():
    exec(open('word2pdf.py').read())

def note():
    exec(open('notemaker.py').read())

def img():
    exec(open('img2pdf.py').read())


btn1 = Button(root, text = 'Convert PDF to WORD', command=conv2doc, height=4,width=25, font=("bold",14),bg="lightsteelblue2")
btn1.place(x='70',y='250') 

btn2 = Button(root, text = 'Convert WORD to PDF', command=conv2pdf, height=4,width=25, font=("bold",14),bg="lightsteelblue2")
btn2.place(x='500',y='250')

btn3 = Button(root, text = 'Note Maker', command=note, height=4,width=25, font=("bold",14),bg="lightsteelblue2")
btn3.place(x='70',y='450')

btn3 = Button(root, text = 'Image converter', command=img, height=4,width=25, font=("bold",14),bg="lightsteelblue2")
btn3.place(x='500',y='450')
 
root.mainloop()
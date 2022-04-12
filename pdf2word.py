
from pdf2docx import Converter
from tkinter import *
import tkinter as tk

root = Tk()

frame1=Canvas(root,bg = "lightsteelblue2",bd=10,width=850,height=100)
frame1.place(x=0,y=0)

frame1.create_text(400, 70, text="Convert PDF to WORD", fill="black", font=('Helvetica 25 bold'))
frame1.pack()
# specify size of window.
root.geometry("850x750+0+0")
root.configure(bg="purple3")

L1 =Label(root,text="Source", width=20,font=("bold",14),bg='purple3',fg="white")
L1.place(x=30,y=200)

 
# Create text widget and specify size.
T1 = Text(root, height = 1, width = 50,font=(13))
T1.place(x=200,y=200)

L2 =Label(root,text="Destination", width=20,font=("bold",14,),bg='purple3',fg="white")
L2.place(x=20,y=400)

 
# Create text widget and specify size.
T2 = Text(root, height = 1, width = 50,font=(13))
T2.place(x=200,y=400)

def convert():
    pdf_file=T1.get(1.0, "end-1c")
    word_file=T2.get(1.0, "end-1c")

    cv= Converter(pdf_file)
    cv.convert(word_file,start=0,end=None)
    cv.close()
  
# Create button and image

btn = Button(root, text = 'Convert', command=convert, height=3,width=15, font=("bold",14))
btn.place(x='350',y='550') 
 
root.mainloop()


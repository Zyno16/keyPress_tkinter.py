from tkinter import ttk
from tkinter import *
from tools import *

form = Tk()
form.geometry("700x500")
tkcenter(form)

txt =ttk.Entry(form)
txt.pack(pady=10)   

def key(event):
    print(event)
    print(".....")
    print(event.__dict__)


txt.bind("<Key>",key)
form.mainloop()


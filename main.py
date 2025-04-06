import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
import os

import functions as func

width = 600
height = 350

root = tk.Tk()

def openNew():
    messagebox.askquestion("New window", "All changes will not be saved")
    if 'yes':
        root.destroy()
        func.openNew()
    else:
        func.nothing()

def closeApp():
    messagebox.askokcancel("Exit", "Are you sure you want to close application?")
    if 'yes':
        root.destroy()
        func.logout()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

dimension = f"{width}x{height}+{x}+{y}"

root.geometry(dimension)
root.title("Main")
root.resizable(0, 0)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=openNew)
filemenu.add_command(label="Open", command=func.nothing)
filemenu.add_command(label="Exit", command=closeApp)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
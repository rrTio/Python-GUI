import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
import os

import functions as func

global items, i
items = []
i = 0

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

def addToList():
    global i
    i += 1
    items.append(f"List item no. {i}")
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

def removeToList():
    if items:
        items.pop()
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

def removeSelected():
    selectedItems = listbox.curselection()
    for index in reversed(selectedItems):
        del items[index]
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)



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
editmenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=openNew)
filemenu.add_command(label="Open", command=func.nothing)
filemenu.add_command(label="Exit", command=closeApp)

editmenu.add_command(label="Add", command=func.nothing)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
root.config(menu=menubar)

root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

fontListText = tkFont.Font(size=12, weight="bold")

listbox = tk.Listbox(root, fg="green", bg="black", justify="center", font=fontListText, selectmode="multiple")
listbox.grid(row=0, column=0, sticky="ew")

btnframe = tk.Frame(root)
btnframe.grid(row=0, column=1, sticky="nsew", pady=2)

btnframe.columnconfigure(0, weight=1)
btnframe.columnconfigure(1, weight=2)
btnframe.columnconfigure(2, weight=1)

tk.Button(btnframe, text="Add", command=addToList).grid(row=0, column=1, sticky="ew", pady=2)
tk.Button(btnframe, text="Remove", command=removeToList).grid(row=1, column=1, sticky="ew", pady=2)
tk.Button(btnframe, text="Delete Selected Items", command=removeSelected).grid(row=2, column=1, sticky="ew", pady=2)


root.mainloop()
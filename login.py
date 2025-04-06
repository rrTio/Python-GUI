import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
import os

username = os.getenv("my_username")
password = os.getenv("my_password")

def checker(event = None):
    if txtUSERNAME.get() == username and txtPASSWORD.get() == password:
        print("VALID")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        open = f'python {script_dir}\\main.py'
        print(open)
        root.destroy()
        os.system(open)
    else:
        messagebox.showerror("LOGIN", "INVALID ACCOUNT")

width = 320
height = 200

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

dimension = f"{width}x{height}+{x}+{y}"

root.geometry(dimension)
root.title("Login")
root.resizable(0, 0)

labelframe = tk.Frame(root, bd=5, relief="solid")
labelframe.pack(fill="x", expand=True)

mainframe = tk.Frame(root, bd=1, relief="solid")
mainframe.pack(fill="both", expand=True, padx=5, pady=5)

mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=2)

mainframe.rowconfigure(1, weight=2)
mainframe.rowconfigure(2, weight=2)
mainframe.rowconfigure(3, weight=3)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=2)

fontObj = tkFont.Font(size=15, weight="bold")
labelfont = tkFont.Font(size=10, weight="bold")
reliefValue = "sunken"
labelReliefValue = "solid"

tk.Label(labelframe, text="USER LOGIN", fg="green", bg="black", font=fontObj).pack(fill="x")

tk.Label(mainframe).grid(row=0, columnspan=4, sticky="nsew") #SPACER

#USERNAME
txtUSERNAME = StringVar()
tk.Label(mainframe, text="Username", fg="green", font=labelfont).grid(row=1, column=1, sticky="nsew", pady=5)
tk.Entry(mainframe, bd=2, relief=reliefValue, textvariable=txtUSERNAME).grid(row=1, column=2, sticky="nsew", pady=5)

#PASSWORD
txtPASSWORD = StringVar()
tk.Label(mainframe, text="Password", fg="green", font=labelfont).grid(row=2, column=1, sticky="nsew")
tk.Entry(mainframe, bd=2, relief=reliefValue, show = "*", textvariable=txtPASSWORD).grid(row=2, column=2, sticky="nsew")

tk.Label(mainframe).grid(row=3, column=0, columnspan=4, sticky="ew") #SPACER

tk.Button(mainframe, text="Login", fg="green", bd=1, relief="ridge", font=labelfont, command=checker).grid(row=4, column=1, columnspan=2, sticky="nsew")

tk.Label(mainframe).grid(row=5, column=0, columnspan=4, sticky="ew") #SPACER

root.mainloop()
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import *
import os
import functions as func

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

def opener(event = None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    open = f'python {script_dir}\\main.py'
    root.destroy()
    os.system(open)

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

labelframe = tk.Frame(root, relief="solid")
labelframe.pack(fill="x", expand=True)

labelframe.columnconfigure(0, weight=1)

mainframe = tk.Frame(root)
mainframe.pack(fill="both", expand=True, padx=5, pady=5)

mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=2)

mainframe.rowconfigure(0, weight=2)
mainframe.rowconfigure(1, weight=2)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)

fontObj = tkFont.Font(size=20, weight="bold")
labelfont = tkFont.Font(size=10, weight="bold")
reliefValue = "sunken"
labelReliefValue = "solid"

tk.Label(labelframe, text="USER LOGIN", fg="green", bg="black", font=fontObj).grid(row=0, column=0, sticky="sew")

#USERNAME
txtUSERNAME = StringVar()
tk.Label(mainframe, text="Username", fg="green", font=labelfont).grid(row=0, column=1, sticky="nsew", pady=5)
tk.Entry(mainframe, bd=2, relief=reliefValue, textvariable=txtUSERNAME).grid(row=0, column=2, sticky="nsew", pady=5)

#PASSWORD
txtPASSWORD = StringVar()
tk.Label(mainframe, text="Password", fg="green", font=labelfont).grid(row=1, column=1, sticky="nsew")
tk.Entry(mainframe, bd=2, relief=reliefValue, show = "*", textvariable=txtPASSWORD).grid(row=1, column=2, sticky="nsew")

tk.Button(mainframe, text="Login", fg="green", bd=2, relief="raised", font=labelfont, command=checker).grid(row=3, column=1, columnspan=2, sticky="nsew", pady=5)

signup = tk.Label(mainframe, text="Sign Up", fg="black", cursor="hand2")
signup.grid(row=4, column=1, columnspan=2, sticky="nsew")
signup.bind("<Button-1>", opener)
root.mainloop()
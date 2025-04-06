from tkinter import messagebox
import os

def nothing():
    x = 0

def logout():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    open = f'python {script_dir}\\login.py'
    os.system(open)

def openNew():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    open = f'python {script_dir}\\main.py'
    os.system(open)

# Importing required libraries here
from tkinter import *  # For importing everything from tkinter to make a GUI interface

from PIL import ImageTk, Image # For showing images with Tkinter

from tkinter import messagebox #For showing popup messages on errors

# _____________________________________________________________

root = Tk()#making the main window for user interaction

root.title('ChemElement Finder')#Setting title of the window

root.geometry('1355x825')#To fix the size and geometry of the window

root.iconbitmap('flaskicon.ico')#Adding a flask shaped icon to the window




mainloop()
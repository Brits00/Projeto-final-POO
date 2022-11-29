#https://www.tutorialspoint.com/python/tk_button.htm

#https://www.tutorialspoint.com/python/python_gui_programming.htm

from tkinter import *
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk


top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()
top.mainloop()



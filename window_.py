from tkinter import *
import tkinter as tk

master = Tk()  # Create the main window
master.title('dictation program')
lst = ["hello", "world"]
# lbl = Label(master, text = "Hello\n\n\n\n\n\n\n", justify=LEFT, anchor = 'e').pack()
# lbl = Label(master, text = "\nworld\n\n\n\n\n\n\n\n\n\nhi").pack()
lbl = Label(master, text="Hello world", relief =SOLID, width = 40, height = 40, anchor = NW, justify=LEFT).pack()

# master.geometry("500x500"
#
#
#
#
# master.update_idletasks()
# master.update()
# print("hello")
lbl2 = Label(master, text = "good morning")
master.mainloop()

from tkinter import *

top = Tk()
frame = Frame(top, width=1000, height=1000)
frame.pack()
frame.place(x=0, y=100)
frame.wm_attributes('-alpha', 0.5)
top.mainloop()

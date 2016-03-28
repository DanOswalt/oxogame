
import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) #what does RIDGE mean
frame.pack(fill=BOTH,expand=1) #what does expand mean
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1) #still not getting the fill property, x, y, both
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop() #does this just mean set the event listener?

from tkinter import *
from PIL import Image

def on_enter(e):
    e.widget["background"] = "green"

def on_leave(e):
    e.widget["background"] = ("white" if e.widget.row%2 != e.widget.column%2 else "black")
    #hovering events

root = Tk()
frame = Frame(root, width=800, height=800, background="white")
frame.pack_propagate(0)
frame.pack()

lab = Label(frame)
lab.pack()

butts = list()
for i in range (8):
    for j in range (8):
        lab.grid(row=i, column=j)
        butt = Button(lab, bg=("white" if i%2 != j%2 else "black"))
        butt.config(height=5, width=8)
        butt.bind("<Enter>", on_enter)
        butt.bind("<Leave>", on_leave)
        butt.grid(row=i, column=j) #creating button grid

root.mainloop()
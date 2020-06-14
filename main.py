from tkinter import *
from PIL import Image

root = Tk()
frame = Frame(root, width=800, height=800, background="white")
frame.pack_propagate(0)
frame.pack()

img = PhotoImage(file="imgs/board.png")
lab = Label(frame, image=img)
lab.pack() #setting board background

butts = list()
for i in range (8):
    for j in range (8):
        lab.grid(row=i, column=j)
        butt = Button(lab)
        butt.config(height=5, width=8)
        butt.grid(row=i, column=j)

root.mainloop()
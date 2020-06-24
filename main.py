import tkinter as tk
from Board import Board
from PIL import Image
from PIL import ImageTk as itk
import numpy as np

def init():
    global root
    global extraref #creates a reference to the pieces images
                    #so they don't get garbage collected
    extraref = np.array([tk.Label() for item in range(64)]).reshape(8, 8)

"""def on_enter(e):
    e.widget["background"] = "green"

def on_leave(e):
    e.widget["background"] = ("white" if e.widget.row%2 != e.widget.column%2 else "black")
    #hovering events"""

def switch(board, val):
    switcher = {
        Board.E: "imgs/E.gif",
        Board.W: "imgs/W.gif",
        Board.B: "imgs/B.gif",
        Board.DW: "imgs/DW.gif",
        Board.DB: "imgs/DB.gif",
    }
    return switcher.get(val)

def refresh(board): #refreshes the board after a turn
    mat = board.getMat()
    #print(mat)
    for i in range(8):
        for j in range(8):
            path = switch(board, mat[i][j])
            #path = "imgs/B.gif"
            tmp_img = Image.open(path)
            img = itk.PhotoImage(tmp_img, master=root)
            
            extraref[i][j] = tk.Label(root)
            extraref[i][j].img = img
            extraref[i][j].config(image = extraref[i][j].img)
            butts[i*8+j].config(image = extraref[i][j].img)

root = tk.Tk()
init()
frame = tk.Frame(root, width=800, height=800, background="white")
frame.pack()
frame.pack_propagate(0)

lab = tk.Label(frame)
lab.pack()

butts = list()
for i in range (8):
    for j in range (8):
        lab.grid(row=i, column=j)
        butt = tk.Button(lab, bg=("black" if i%2 != j%2 else "white"))
        #butt.config(height=5, width=8)
        #butt.bind("<Enter>", on_enter)
        #butt.bind("<Leave>", on_leave)
        butts.append(butt)
        butt.grid(row=i, column=j) #creating button grid

board = Board()
refresh(board) #places pieces on the grid

root.mainloop()
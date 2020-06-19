import tkinter as tk
from Board import Board
from PIL import Image
from PIL import ImageTk as itk

"""def on_enter(e):
    e.widget["background"] = "green"

def on_leave(e):
    e.widget["background"] = ("white" if e.widget.row%2 != e.widget.column%2 else "black")
    #hovering events"""

def switch(board, val):
    switcher = {
        Board.E: "imgs/E.png",
        Board.W: "imgs/W.png",
        Board.B: "imgs/B.png",
        Board.DW: "imgs/DW.png",
        Board.DB: "imgs/DB.png",
    }
    return switcher.get(val)

def refresh(board): #refreshes the board after a turn
    mat = board.getMat()
    for i in range(8):
        for j in range(8):
            tmp_img = Image.open(switch(board, mat[i][j]))
            img = itk.PhotoImage(tmp_img)
            butts[i*8+j].configure(image = img)
            #butts[i*8+j].pack()

root = tk.Tk()
frame = tk.Frame(root, width=800, height=800, background="white")
frame.pack_propagate(0)
frame.pack()

lab = tk.Label(frame)
lab.pack()

butts = list()
for i in range (8):
    for j in range (8):
        lab.grid(row=i, column=j)
        butt = tk.Button(lab, bg=("white" if i%2 != j%2 else "black"))
        #butt.config(height=5, width=8)
        #butt.bind("<Enter>", on_enter)
        #butt.bind("<Leave>", on_leave)
        butts.append(butt)
        butt.grid(row=i, column=j) #creating button grid

board = Board()
refresh(board) #places pieces on the grid

root.mainloop()
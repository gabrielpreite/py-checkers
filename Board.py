import numpy as np

class Board:
    E = 0
    W = 1
    B = 2
    DW = 3
    DB = 4

    def __init__(self):
        self.mat = np.zeros((8,8))
        for i in range(8):
            for j in range(8):
                if(i<3 and i%2!=j%2):
                    self.mat[i][j] = Board.B
                elif(i>4 and i%2!=j%2):
                    self.mat[i][j] = Board.W
        #print(mat)

    def getMat(self):
        return self.mat
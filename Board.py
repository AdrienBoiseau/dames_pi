from Piece import *
from AtomicMove import *

class Board:
    def __init__(self, size):
        self.size=size
        self.play_board=[['.' for i in range(size)] for j in range(size)]

        for i in range(0,self.size,2):
            for j in range(0,self.size,2):
                self.play_board[i][j]='_'

        for i in range(1,self.size,2):
            for j in range(1,self.size,2):
                self.play_board[i][j]='_'

        for i in range(0,self.size//2-1,2):
            for j in range(0,self.size,2):
                self.play_board[i][j]=Piece((i,j),'B')

        for i in range(1,self.size//2-1,2):
            for j in range(1,self.size,2):
                self.play_board[i][j]=Piece((i,j),'B')

        if self.size//2 %2:
            x=0
            y=1
        else:
            x=1
            y=0

        for i in range(self.size//2+1,self.size,2):
            for j in range(x,self.size,2):
                self.play_board[i][j]=Piece((i,j),'N')

        for i in range(self.size//2+2,self.size,2):
            for j in range(y,self.size,2):
                self.play_board[i][j]=Piece((i,j),'N')


    def to_lines(self):
        print('Jeu de Dames : \n')
        print('   ', end='')
        for i in range(self.size):
            print('', i, '', end='')
        print()
        for i in range(self.size):
            print(i,'[', end='')
            for j in range(self.size):
                if self.play_board[i][j]== '.' or self.play_board[i][j]== '_' :
                    print('',self.play_board[i][j],'', end='')
                else:
                    print('', self.play_board[i][j].get_color(), '', end='')
            print(']')
        print()
        return




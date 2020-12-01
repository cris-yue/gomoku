
N = 15

class Gomoku:
    def __init__(self):
        self.board = [[None] * N for i in range(N)]
        self.turn = "x"
        self.winner = None

    def get_moves(self):
        ret = []
        for it, row in enumerate(self.board):
            for jt, cell in enumerate(row):
                if cell == None:
                    ret.append([it,jt])
        return ret


    def __str__(self):
        ret = ''
        for row in self.board:
            for cell in row:
                if cell == None:
                    ret += " "
                elif cell == "x":
                    ret += "x"
                elif cell == "o":
                    ret += "o"
                else:
                    raise ValueError("Invalid character in the board")
            ret += "\n"
        return ret
    __repr__ = __str__


    def make_move(self,x,y):
        if self.board[x][y] != None:
            raise ValueError("place occupied")
        self.board[x][y] = self.turn
        self.turn = 'x' if self.turn == 'o' else 'o'

    def game_over(self):
        if len(self.get_moves()) == 0:
            self.winner = 0
            return True
        for i in range(N):
            for j in range(N):
                if self.board[i][j] != None and j< N-4: # horizontal
                    win = True
                    for k in range(1,5):
                        if self.board[i][j+k] != self.board[i][j]:
                            win = False
                            break
                    if win:
                        self.winner = 1 if self.board[i][j] == 'x' else 2
                        return True
                if self.board[i][j] != None and i < N-4: #vertical
                    win = True
                    for k in range(1,5):
                        if self.board[i+k][j] != self.board[i][j]:
                            win = False
                            break
                    if win:
                        self.winner = 1 if self.board[i][j] == 'x' else 2
                        return True
                if self.board[i][j] != None and 4 < i and j< N-4: #right diagonal
                    win = True
                    for k in range(1,5):
                        if self.board[i-k][j+k] != self.board[i][j]:
                            win = False
                            break
                    if win:
                        self.winner = 1 if self.board[i][j] == 'x' else 2
                        return True
                if self.board[i][j] != None and i < N-4 and j< N-4: #left diagonal
                    win = True
                    for k in range(1,5):
                        if self.board[i+k][j+k] != self.board[i][j]:
                            win = False
                            break
                    if win:
                        self.winner = 1 if self.board[i][j] == 'x' else 2
                        return True
        return False

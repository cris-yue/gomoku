import random, pdb, copy, time
import numpy as np
N=15

class MiniMaxTimeout(Exception):
    pass

class MiniMaxAI:
    def __init__(self,player_one, timeout = 5.0):
        self.player_one = player_one
        self.distance_Matrix = [
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
            [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7],
            [7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7],
            [7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 7],
            [7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7],
            [7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7],
            [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
        ]

        self.start = None
        self.timeout = timeout

    def make_move(self, game):
        ret = None
        self.start = time.time()
        try:
            for depth in range(1,10**1000):
                ret = self.minimax(game,depth=0,max_depth=depth)
        except MiniMaxTimeout:
            print(f"ply = {depth}")
            if ret == None:
                return random.choice(game.get_moves())
            else:
                return ret

    def minimax(self,game,depth = 0, max_depth=1):
        if time.time() - self.start > self.timeout:
            raise MiniMaxTimeout

        if depth == max_depth or game.game_over():
            return self.evaluate(game)
        scores = {}
        for move in game.get_moves():
            new_game = copy.deepcopy(game)
            new_game.make_move(x=move[0],y=move[1])
            scores[tuple(move)] = self.minimax(game=new_game,depth=depth+1,max_depth=max_depth)
        key = lambda p: scores[p] if scores[p] != None else 0
        if depth % 2 == 0:
            if depth == 0:
                return max(scores,key=key)
            return scores[max(scores,key=key)]
        else:
            return scores[min(scores,key=key)]

    def evaluate(self, game):
        if game.game_over():
            if   game.winner == 0: return 0.0
            elif game.winner == 1: return float('inf') if self.player_one else float('-inf')
            else: return float('inf') if not self.player_one else float('-inf')
        ret = 0
        ret += self.center_metric(game)
        ret += self.random_metric(game)
        return ret

    def center_metric(self,game):
        alpha = 0.95
        score_me, score_opp, n_me, n_opp = 0, 0, 0, 0
        for i, row in enumerate(game.board):
            for j, cell in enumerate(row):
                if cell == None: continue
                elif (self.player_one and cell == 'x') or (not self.player_one and cell == 'o'):
                    score_me += alpha ** self.distance_Matrix[i][j]
                    n_me += 1
                else:
                    score_opp += alpha ** self.distance_Matrix[i][j]
                    n_opp += 1
        return (score_me / n_me if n_me != 0 else 0) - (score_opp / n_opp if n_opp != 0 else 0)
        #sum(alpha)^

    def neighbor_metric(self,game):
        score_me, score_opp, n_me, n_opp = 0, 0, 0, 0
        player = 'x' if self.player_one else 'o'

        for i, row in enumerate(game.board):
            for j, cell in enumerate(row):
                if cell == None: continue
                elif cell == player:
                    n_me += 1

                else:

        return (score_me / n_me if n_me != 0 else 0) - (score_opp / n_opp if n_opp != 0 else 0)




    def random_metric(self,game):
        return np.random.normal(0,10**-5)
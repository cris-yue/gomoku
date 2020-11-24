import random, pdb

N=15
class MiniMaxAI:
    def __init__(self,player_one):
        self.player_one = player_one
        self.distance_Matrix = [
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
            [6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
            [6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6],
            [6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 2, 2, 2, 2, 2, 3, 4, 5, 6],
            [6, 5, 4, 3, 3, 3, 3, 3, 3, 3, 4, 5, 6],
            [6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6],
            [6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
            [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        ]


    def make_move(self, game):
        return random.choice(game.get_moves())
    def evaluate(self, game):
        ret = 0
        ret += self.center_metric(game)
        #ret += self.metric2(game)
        #ret += self.metric3(game)

        return ret
    def center_metric(self,game):
        alpha = 0.95
        #sum(alpha)^

import random
class RandomAI:
    def __init__(self,player_one):
        self.player_one = player_one
    def make_move(self, game):
        return random.choice(game.get_moves())
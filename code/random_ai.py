import random
class RandomAI:
    def __init__(self):
        pass
    def make_move(self, game):
        return random.choice(game.get_moves())
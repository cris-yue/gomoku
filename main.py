# This is a sample Python script.

from code.gomoku import Gomoku
import random, sys, traceback, pdb
from code.random_ai import RandomAI
from code.minimax_ai import MiniMaxAI

def main():
    # Use a breakpoint in the code line below to debug your script.
     # Press ⌘F8 to toggle the breakpoint.

    game = Gomoku()
    player1 = MiniMaxAI(player_one=True,timeout=10.0)
    player2 = MiniMaxAI(player_one=False,timeout=10.0)
    while not game.game_over():
        if game.turn == 'x':
            move = player1.make_move(game)
        else:
            move = player2.make_move(game)
        game.make_move(move[0], move[1])
        print(game)
        #input('=' * 50)


    print("Done :)")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main()
        print("Completed evaluation without error.")
    except:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

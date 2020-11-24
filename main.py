# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from code.gomoku import Gomoku
import random
from code.random_ai import RandomAI

def main():
    # Use a breakpoint in the code line below to debug your script.
     # Press ⌘F8 to toggle the breakpoint.

    game = Gomoku()
    player1 = RandomAI()
    player2 = RandomAI()
    while not game.game_over():
        if game.turn == 'x':
            move = player1.make_move(game)
        else:
            move = player2.make_move(game)
        game.make_move(move[0], move[1])
        print(game)
        input('=' * 50)


    print("Done :)")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from code.gomoku import Gomoku
import random

def main():
    # Use a breakpoint in the code line below to debug your script.
     # Press ⌘F8 to toggle the breakpoint.

    game = Gomoku()
    while not game.game_over():
        try:
            x = random.randint(0,14)
            y = random.randint(0,14)
            game.make_move(x,y)
            print(game)
            input('===' * 20)
        except ValueError as e:
            continue
    print("Done :)")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

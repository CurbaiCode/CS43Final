import random

symbols = ["X", "O"]

class Game:

    def __init__(self, name1, symbol1, name2, symbol2):
        self.board = Board()
        self.p1 = Player(name1, symbol1)
        self.p2 = Player(name2, symbol2)

    def display_board(self):
        self.board.display()


class Board:

    def __init__(self):
        self.square = {
            "7": " ", "8": " ", "9": " ",
            "4": " ", "5": " ", "6": " ",
            "1": " ", "2": " ", "3": " "
        }

    def display(self):
        print(self.square["7"] + "|" + self.square["8"] + "|" + self.square["9"])
        print("-+-+-")
        print(self.square["4"] + "|" + self.square["5"] + "|" + self.square["6"])
        print("-+-+-")
        print(self.square["1"] + "|" + self.square["2"] + "|" + self.square["3"])


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


n1 = input("What's player 1's name? ")
n2 = input("What's player 2's name? ")
if random.choice(range(2)) == 0:
    s1 = input("{}, pick a symbol (X/O): ".format(n1))
    s2 = symbols[int(not bool(symbols.index(s1)))]
else:
    s2 = input("{}, pick a symbol (X/O): ".format(n2))
    s1 = symbols[int(not bool(symbols.index(s2)))]

g = Game(n1, s1, n2, s2)
g.display_board()

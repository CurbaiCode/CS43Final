import random

sym = ["X", "O"]
names = ["", ""]
symbols = ["", ""]

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

    def instructions(self):
        print("How to Play")


class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0


names[0] = input("What's player 1's name? ")
names[1] = input("What's player 2's name? ")
if random.choice(range(2)) == 0:
    symbols[0] = input("{}, pick a symbol (X/O): ".format(names[0])).upper()
    symbols[1] = sym[int(not bool(sym.index(symbols[0])))]
    currentP = 1
    nextP = 0
else:
    symbols[1] = input("{}, pick a symbol (X/O): ".format(names[1])).upper()
    symbols[0] = sym[int(not bool(sym.index(symbols[1])))]
    currentP = 0
    nextP = 1

g = Game(names[0], symbols[0], names[1], symbols[1])
g.display_board()
move = input("{}, what's your move? ".format(names[currentP]))

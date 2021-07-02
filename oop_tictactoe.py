import random

symbols = ["X", "O"]

class Game:

    def __init__(self):
        self.board = Board()
        self.p1 = Player(0)
        self.p2 = Player(1)
        if random.choice(range(2)) == 0:
            self.p1.setSymbol()
            self.p2.sym = symbols[int(not bool(symbols.index(self.p1.sym)))]
            self.cur = self.p2
            self.next = self.p1
        else:
            self.p2.setSymbol()
            self.p1.sym = symbols[int(not bool(symbols.index(self.p2.sym)))]
            self.cur = self.p1
            self.next = self.p2

    def displayBoard(self):
        self.board.display()

    def instructions(self):
        print("How to Play")

    def makeMove(self, player, square):
        while self.board.update(player.sym, square) is None:
            square = input("Sorry {}, you can't move there. Try again: ".format(player.name))

        return self.board.update(player.sym, square)

    def isWon(self, player):
        return self.board.isWinner(player)

    def isDraw(self):
        return self.board.noMoves()

    def switchTurns(self):
        self.cur, self.next = self.next, self.cur


class Board:

    def __init__(self):
        self.squares = {
            "7": " ", "8": " ", "9": " ",
            "4": " ", "5": " ", "6": " ",
            "1": " ", "2": " ", "3": " "
        }

    def display(self):
        print()
        print(self.squares["7"] + "|" + self.squares["8"] + "|" + self.squares["9"])
        print("-+-+-")
        print(self.squares["4"] + "|" + self.squares["5"] + "|" + self.squares["6"])
        print("-+-+-")
        print(self.squares["1"] + "|" + self.squares["2"] + "|" + self.squares["3"])

    def squareEmpty(self, square):
        if square in self.squares and self.squares[square] == " ":
            return True

        return False

    def update(self, symbol, square):
        if self.squareEmpty(square):
            self.squares[square] = symbol
            return self.squares

        return None

    def isWinner(self, player):
        possibleWins = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["7", "4", "1"],
            ["8", "5", "2"],
            ["9", "6", "3"],
            ["7", "5", "3"],
            ["1", "5", "9"]
        ]
        for x, y, z in possibleWins:
            if self.squares[x] == self.squares[y] == self.squares[z] == player.sym:
                return True

        return False

    def noMoves(self):
        for square in self.squares:
            if self.squares[square] == " ":
                return False

        return True


class Player:

    def __init__(self, number):
        self.name = input("What's player {}'s name? ".format(str(number + 1)))
        self.sym = ""
        self.score = 0

    def validSymbol(self, symbol):
        if symbol in symbols:
            return True

        return False

    def setSymbol(self):
        symbol = input("{}, pick a symbol ({}/{}): ".format(self.name, symbols[0], symbols[1])).upper()
        while self.validSymbol(symbol) is False:
            symbol = input("That's not a valid symbol {}, pick \"{}\" or \"{}\": ".format(self.name, symbols[0], symbols[1])).upper()

        self.sym = symbol


g = Game()
while True:
    g.displayBoard()
    move = input("{}, what's your move? ".format(g.cur.name))
    g.makeMove(g.cur, move)
    if g.isWon(g.cur):
        g.displayBoard()
        print("{} wins!".format(g.cur.name))
        break
    elif g.isDraw():
        g.displayBoard()
        print("Draw!")
        break

    g.switchTurns()

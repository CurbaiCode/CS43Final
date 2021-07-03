import random

symbols = ["X", "O"]

class Game:

    def __init__(self):
        self.menu()
        self.board = Board()
        self.p1 = Player(1)
        self.p2 = Player(2)
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

    def validSelection(self, selection):
        if selection in map(str, range(4)):
            return True

        return False

    def displayBoard(self):
        self.board.display()

    def menu(self):
        global symbols
        print("""{0}{0}{0}{0}{0}{0} {1}{1}       {1}{1}{1}{1}{1}{1}            {0}{0}{0}{0}{0}{0}            
  {0}{0}              {1}{1}                {0}{0}         {0}{0}{0}{0} 
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}  {0}{0}  {0}{0}
  {0}{0}   {1}{1} {0}{0}      {1}{1} {0}{0}  {0}{0} {1}{1}      {0}{0} {1}{1}  {1}{1} {0}{0}{0}{0}  
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}   {0}{0}{0}{0}{0}

                  1) Start Game  
                  2) How To Play 
                  3) Exit        
""".format(symbols[0], symbols[1]))
        selection = input("Select an option: ")
        while self.validSelection(selection) is False:
            selection = input("Please select an option from the menu above: ")

        if selection == "1":
            return
        elif selection == "2":
            self.instructions()
            return
        elif selection == "3":
            raise SystemExit
        elif selection == "0":
            print()
            print("You found an Easter Egg!")
            symbols = input("Enter new symbols separated by a space e.g. \"X O\": ").upper().split(" ")
            print()
            self.menu()
        else:
            print("An unexpected error has occurred.")


    def instructions(self):
        print("""
Welcome to Tic-Tac-Toe!

##/ The Screen /#########################

                     You can place a 
         symbol in this empty square 
      /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
     /   You can't move in 
    /   an occupied square 
   / /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯       7|8|9 
{0}̲| |{1}                             -+-+- 
-+-+-    The board is laid out    4|5|6 
 |{0}̲|{0}    like a numeric keypad  / -+-+- 
-+-+- <¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯  1|2|3 
{1}|{1}|{0}̲ 
     \        When the game is won, the 
      \  winning symbols are underlined 
       ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
Press ENTER to continue... """.format(symbols[0], symbols[1]), end="")
        input()
        print("""
##/ Instructions /######################
The goal of Tic-Tac-Toe is to be the    
first player to get three of your       
symbols in a row on the board.          

Press ENTER to continue... """, end="")
        input()
        print("""
Players alternate placing {0}s and {1}s on  
the board until either player has three 
in a row, across, down, or diagonally   
or until all squares on the board are   
filled. If a player is able to place    
three {0}s or three {1}s in a row, then     
that player wins. If all squares are    
filled and neither player has made a    
complete row of {0}s or {1}s, then the game 
is a draw.                              

Press ENTER to continue... """.format(symbols[0], symbols[1]), end="")
        input()
        print("""
Players make their moves by entering       
the number that corresponds with the      
square they wish to place their symbol    
in. Players can not place their symbol in 
a square which is occupied by any symbol, 
whether it is their own or not.           

Press ENTER to start! """, end="")
        input()
        print()

    def makeMove(self, player, square):
        while self.board.update(player.sym, square) is None:
            square = input("Sorry {}, you can't move there. Try again: ".format(player.name))

        return self.board.update(player.sym, square)

    def isWon(self, player):
        return self.board.isWinner(player)

    def isDraw(self):
        return self.board.noMoves()

    def scoreboard(self):
        print("""
================================
           SCOREBOARD           
================================
    {:<16} {:<7}    
    {:<16} {:<7}    
================================""".format(self.p1.name, self.p1.score, self.p2.name, self.p2.score))

    def switchTurns(self):
        self.cur, self.next = self.next, self.cur

    def isOver(self):
        if self.board.donePlaying() is False:
            self.board.reset()
            return False

        return True


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

    def validSquare(self, square):
        if square in self.squares and self.squares[square] == " ":
            return True

        return False

    def update(self, symbol, square):
        if self.validSquare(square):
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
                self.squares[x] = self.squares[y] = self.squares[z] = (player.sym + "̲")
                player.score += 1
                return True

        return False

    def noMoves(self):
        for square in self.squares:
            if self.squares[square] == " ":
                return False

        return True

    def donePlaying(self):
        print()
        return not input("Do you want to play again? (Yes/No): ").lower().startswith("y")

    def reset(self):
        for square in self.squares:
            self.squares[square] = " "

        return self.squares


class Player:

    def __init__(self, number):
        self.name = input("What's player {}'s name? ".format(number))
        self.sym = ""
        self.score = 0

    def validSymbol(self, symbol):
        if symbol in symbols:
            return True

        return False

    def setSymbol(self):
        symbol = input("{}, pick a symbol ({}/{}): ".format(self.name, symbols[0], symbols[1])).upper()
        while self.validSymbol(symbol) is False:
            symbol = input("{}, please pick \"{}\" or \"{}\": ".format(self.name, symbols[0], symbols[1])).upper()

        self.sym = symbol


g = Game()
while True:
    g.displayBoard()
    move = input("{}, what's your move? ".format(g.cur.name))
    g.makeMove(g.cur, move)
    if g.isWon(g.cur):
        g.displayBoard()
        print("{} wins!".format(g.cur.name))
        g.scoreboard()
        if g.isOver():
            break
    elif g.isDraw():
        g.displayBoard()
        print("Draw!")
        g.scoreboard()
        if g.isOver():
            break

    g.switchTurns()

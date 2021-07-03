import random

Symbols = ["X", "O"]

class Game:

    def __init__(self):
        self.Menu()
        self.Board = Board()
        self.P1 = Player(1)
        self.P2 = Player(2)
        if random.choice(range(2)) == 0:
            self.P1.SetSymbol()
            self.P2.Sym = Symbols[int(not bool(Symbols.index(self.P1.Sym)))]
            self.Cur = self.P2
            self.Next = self.P1
        else:
            self.P2.SetSymbol()
            self.P1.Sym = Symbols[int(not bool(Symbols.index(self.P2.Sym)))]
            self.Cur = self.P1
            self.Next = self.P2

    def ValidSelection(self, Selection):
        if Selection in map(str, range(4)):
            return True

        return False

    def DisplayBoard(self):
        self.Board.Display()

    def Menu(self):
        global Symbols
        print("""{0}{0}{0}{0}{0}{0} {1}{1}       {1}{1}{1}{1}{1}{1}            {0}{0}{0}{0}{0}{0}            
  {0}{0}              {1}{1}                {0}{0}         {0}{0}{0}{0} 
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}  {0}{0}  {0}{0}
  {0}{0}   {1}{1} {0}{0}      {1}{1} {0}{0}  {0}{0} {1}{1}      {0}{0} {1}{1}  {1}{1} {0}{0}{0}{0}  
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}   {0}{0}{0}{0}{0}

                  1) Start Game  
                  2) How To Play 
                  3) Exit        
""".format(Symbols[0], Symbols[1]))
        Selection = input("Select an option: ")
        while self.ValidSelection(Selection) is False:
            Selection = input("Please select an option from the menu above: ")

        if Selection == "1":
            return
        elif Selection == "2":
            self.Instructions()
            return
        elif Selection == "3":
            raise SystemExit
        elif Selection == "0":
            print()
            print("You found an Easter Egg!")
            Symbols = input("Enter new symbols separated by a space e.g. \"X O\": ").upper().split(" ")
            print()
            self.Menu()
        else:
            print("An unexpected error has occurred.")

    def Instructions(self):
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
Press ENTER to continue... """.format(Symbols[0], Symbols[1]), end="")
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

Press ENTER to continue... """.format(Symbols[0], Symbols[1]), end="")
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

    def MakeMove(self):
        Square = input("{}, what's your move? ".format(self.Cur.Name))
        while self.Board.Update(self.Cur.Sym, Square) is None:
            Square = input("Sorry {}, you can't move there. Try again: ".format(self.Cur.Name))

        return self.Board.Update(self.Cur.Sym, Square)

    def IsWon(self):
        return self.Board.IsWinner(self.Cur)

    def IsDraw(self):
        return self.Board.NoMoves()

    def DisplayScores(self):
        print("""
================================
           SCOREBOARD           
================================
    {:<16} {:<7}    
    {:<16} {:<7}    
================================""".format(self.P1.Name, self.P1.Score, self.P2.Name, self.P2.Score))

    def SwitchTurn(self):
        self.Cur, self.Next = self.Next, self.Cur

    def IsOver(self):
        if self.Board.DonePlaying() is False:
            self.Board.Reset()
            return False

        return True


class Board:

    def __init__(self):
        self.Squares = {
            "7": " ", "8": " ", "9": " ",
            "4": " ", "5": " ", "6": " ",
            "1": " ", "2": " ", "3": " "
        }

    def Display(self):
        print()
        print(self.Squares["7"] + "|" + self.Squares["8"] + "|" + self.Squares["9"])
        print("-+-+-")
        print(self.Squares["4"] + "|" + self.Squares["5"] + "|" + self.Squares["6"])
        print("-+-+-")
        print(self.Squares["1"] + "|" + self.Squares["2"] + "|" + self.Squares["3"])

    def ValidSquare(self, Square):
        if Square in self.Squares and self.Squares[Square] == " ":
            return True

        return False

    def Update(self, Symbol, Square):
        if self.ValidSquare(Square):
            self.Squares[Square] = Symbol
            return self.Squares

        return None

    def IsWinner(self, Player):
        PossibleWins = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["7", "4", "1"],
            ["8", "5", "2"],
            ["9", "6", "3"],
            ["7", "5", "3"],
            ["1", "5", "9"]
        ]
        for X, Y, Z in PossibleWins:
            if self.Squares[X] == self.Squares[Y] == self.Squares[Z] == Player.Sym:
                self.Squares[X] = self.Squares[Y] = self.Squares[Z] = (Player.Sym + "̲")
                Player.Score += 1
                return True

        return False

    def NoMoves(self):
        for Square in self.Squares:
            if self.Squares[Square] == " ":
                return False

        return True

    def DonePlaying(self):
        print()
        return not input("Do you want to play again? (Yes/No): ").upper().startswith("Y")

    def Reset(self):
        for Square in self.Squares:
            self.Squares[Square] = " "

        return self.Squares


class Player:

    def __init__(self, Number):
        self.Name = input("What's player {}'s name? ".format(Number))
        self.Sym = ""
        self.Score = 0

    def ValidSymbol(self, Symbol):
        if Symbol in Symbols:
            return True

        return False

    def SetSymbol(self):
        Symbol = input("{}, pick a symbol ({}/{}): ".format(self.Name, Symbols[0], Symbols[1])).upper()
        while self.ValidSymbol(Symbol) is False:
            Symbol = input("{}, please pick \"{}\" or \"{}\": ".format(self.Name, Symbols[0], Symbols[1])).upper()

        self.Sym = Symbol


G = Game()
while True:
    G.DisplayBoard()
    G.MakeMove()
    if G.IsWon():
        G.DisplayBoard()
        print("\n{} wins!".format(G.Cur.Name))
        G.DisplayScores()
        if G.IsOver():
            break

    elif G.IsDraw():
        G.DisplayBoard()
        print("\nDraw!")
        G.DisplayScores()
        if G.IsOver():
            break

    G.SwitchTurn()

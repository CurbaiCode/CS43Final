# Imports
import random

# Constants
Symbols = ["X", "O"]
PossibleWins = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["7", "4", "1"],
    ["8", "5", "2"],
    ["9", "6", "3"],
    ["7", "5", "3"],
    ["1", "5", "9"]
]  # All possible ways to win
CPU = "The Computer"

# Functions
def Instructions():
    print("""
Welcome to Tic-Tac-Toe!

##/ The Screen /#########################

                        You can place a  
            symbol in this empty square  
         /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯ 
        /     You can't move in 
       /     an occupied square 
      /   /¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯         7 | 8 | 9  
 {0}̲ |   | {1}                              ---+---+--- 
---+---+---    The board is laid out     4 | 5 | 6  
   | {0}̲ | {0}     like a numeric keypad  / ---+---+--- 
---+---+--- <¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   1 | 2 | 3  
 {1} | {1} | {0}̲  
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

def Multiplayer():
    return input("Would you like to play against a friend? (Yes/No): ").upper().startswith("Y")  # Ask if multiplayer

def DonePlaying():  # Ask if the players want to play another round
    print()
    return not input("Do you want to play again? (Yes/No): ").upper().startswith("Y")

# Classes
class Game:

    def __init__(self):
        self.Menu()  # Display main menu
        self.Board = Board()  # Create 3x3 board
        MultiP = Multiplayer()  # Ask if single or multiplayer
        if MultiP:
            self.P1 = Player(1)  # Create Player 1
            self.P2 = Player(2)  # Create Player 2
            if random.choice(range(2)) == 0:  # Randomly select player
                self.P1.SetSymbol()  # Ask player for symbol
                self.P2.Sym = Symbols[int(not bool(Symbols.index(self.P1.Sym)))]  # Assign the other symbol
                self.Cur = self.P2  # Set which player is the current player
                self.Next = self.P1  # The other player is up next
            else:
                self.P2.SetSymbol()  # Ask player for symbol
                self.P1.Sym = Symbols[int(not bool(Symbols.index(self.P2.Sym)))]  # Assign the other symbol
                self.Cur = self.P1  # Set which player is the current player
                self.Next = self.P2  # The other player is up next

        else:
            self.P1 = Player()  # Create player
            self.P2 = Computer()  # Create computer
            self.P1.SetSymbol()  # Ask player for symbol
            self.P2.Sym = Symbols[int(not bool(Symbols.index(self.P1.Sym)))]  # Assign the other symbol
            self.Cur = self.P1  # Set which player is the current player
            self.Next = self.P2  # The other player is up next

    def ValidSelection(self, Selection):
        if Selection in map(str, range(4)):  # If the player chose a number between 0 and 3
            return True  # Selection is valid

        return False  # Selection is invalid

    def DisplayBoard(self):
        self.Board.Display()

    def Menu(self):  # Main menu
        global Symbols
        print("""
{0}{0}{0}{0}{0}{0} {1}{1}       {1}{1}{1}{1}{1}{1}            {0}{0}{0}{0}{0}{0}            
  {0}{0}              {1}{1}                {0}{0}         {0}{0}{0}{0} 
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}  {0}{0}  {0}{0}
  {0}{0}   {1}{1} {0}{0}      {1}{1} {0}{0}  {0}{0} {1}{1}      {0}{0} {1}{1}  {1}{1} {0}{0}{0}{0}  
  {0}{0}   {1}{1}  {0}{0}{0}{0}   {1}{1}  {0}{0}{0} {0}  {1}{1}{1}{1}   {0}{0}  {1}{1}{1}{1}   {0}{0}{0}{0}{0}

                  1) Start Game  
                  2) How To Play 
                  3) Exit        
""".format(Symbols[0], Symbols[1]))  # Title and menu
        Selection = input("Select an option: ")  # Get selection
        while self.ValidSelection(Selection) is False:  # Validate selection
            Selection = input("Please select an option from the menu above: ")  # If selection is invalid

        # If move is valid
        if Selection == "1":  # "Start Game"
            return
        elif Selection == "2":  # "How To Play"
            Instructions()  # Show instructions before starting the game
            return
        elif Selection == "3":  # "Exit"
            raise SystemExit
        elif Selection == "0":  # Easter Egg
            print()
            print("You found an Easter Egg!")
            while True:
                try:
                    Symbols = input("Enter new symbols separated by a space e.g. \"X O\": ").upper().split(" ")  # Redefine "Symbols" constant
                    Symbols = [Symbol[0] for Symbol in Symbols]  # Get first character of each string
                    self.Menu()  # Go back to main menu
                except Exception:
                    pass

        else:
            print("An unexpected error has occurred.")

    def MakeMove(self):
        if self.Cur.Name == CPU:  # If the computer is making a move
            Square = self.P2.ComputerMove(self.Board.Squares, self.P1.Sym)
            print("{}'s move is {}.".format(CPU, Square))
        else:  # A player is making a move
            Square = input("{}, what's your move? ".format(self.Cur))  # Ask player for move
            while self.Board.Update(self.Cur.Sym, Square) is None:  # Validate move
                Square = input("Sorry {}, you can't move there. Try again: ".format(self.Cur))  # If move is invalid

        return self.Board.Update(self.Cur.Sym, Square)  # If move is valid

    def IsWon(self):
        return self.Board.IsWinner(self.Cur)  # Determine if current player is the winner

    def IsDraw(self):
        return self.Board.NoMoves()  # Determine if there are no more valid moves left

    def DisplayScores(self):
        print("""
================================
           SCOREBOARD           
================================
    {:<16} {:<7}    
    {:<16} {:<7}    
================================""".format(self.P1.Name, self.P1.Score, self.P2.Name, self.P2.Score))

    def SwitchTurn(self):
        self.Cur, self.Next = self.Next, self.Cur  # Make the current player next and the next player current

    def IsOver(self):
        if DonePlaying() is False:  # If the players are not done playing
            self.Board.Reset()
            return False  # The game is not over

        return True  # The game is over


class Board:

    def __init__(self):
        self.Squares = {
            "7": " ", "8": " ", "9": " ",
            "4": " ", "5": " ", "6": " ",
            "1": " ", "2": " ", "3": " "
        }  # Create a blank 3x3 board with the correct key equivalents

    def Display(self):  # Display the board
        print()
        print(" {} | {} | {} ".format(self.Squares["7"], self.Squares["8"], self.Squares["9"]))
        print("---+---+---")
        print(" {} | {} | {} ".format(self.Squares["4"], self.Squares["5"], self.Squares["6"]))
        print("---+---+---")
        print(" {} | {} | {} ".format(self.Squares["1"], self.Squares["2"], self.Squares["3"]))

    def ValidSquare(self, Square):
        if Square in self.Squares and self.Squares[Square] == " ":  # If the given square exists and is blank
            return True  # Square is valid move

        return False  # Square is invalid move

    def Update(self, Symbol, Square):  # Update the state of the board with the given move
        if self.ValidSquare(Square):  # If the move is valid
            self.Squares[Square] = Symbol  # Place the player's symbol on the board in the correct square
            return self.Squares  # Return the layout of the board

        return None

    def IsWinner(self, Player):  # Determine if the given player is the winner
        for X, Y, Z in PossibleWins:  # For each square in every possible win
            if self.Squares[X] == self.Squares[Y] == self.Squares[Z] == Player.Sym:  # If all squares in a row contain the player's symbol
                self.Squares[X] = self.Squares[Y] = self.Squares[Z] = (Player.Sym + "̲")  # Mark the symbols with an underline
                Player.Score += 1  # Add the win to the player's score
                return True  # The player has won

        return False  # The player hasn't won

    def NoMoves(self):  # Determine if the are no more empty squares on the board
        for Square in self.Squares:
            if self.Squares[Square] == " ":  # If any square is blank
                return False  # There are still possible moves

        return True  # The board is completely full

    def Reset(self):  # Clear the board
        for Square in self.Squares:
            self.Squares[Square] = " "  # Make all the squares blank

        return self.Squares  # Return the layout of the board


class Player:

    def __init__(self, Number=0):
        if Number == 0:  # If the player is the only player
            self.Name = input("What is your name? ")  # Ask for player name
            while self.Name == "CPU":  # Easter Egg
                global CPU
                print()
                print("You found an Easter Egg!")
                CPU = input("Enter new computer name: ")  # Redefine "CPU" constant
                print()
                self.Name = input("What is your name? ")

        else:  # There are multiple players
            self.Name = input("What's player {}'s name? ".format(Number))  # Ask for player name

        self.Sym = ""  # Initialize the player's symbol
        self.Score = 0  # Set the score to 0 wins

    def __str__(self):
        return self.Name  # Return player's name when referenced without properties

    def ValidSymbol(self, Symbol):
        if Symbol in Symbols:  # If given symbol is in "Symbols" constant
            return True  # The symbol is valid

        return False  # The symbol is invalid

    def SetSymbol(self):
        Symbol = input("{}, pick a symbol ({}/{}): ".format(self.Name, Symbols[0], Symbols[1])).upper()  # Ask for symbol
        while self.ValidSymbol(Symbol) is False:  # Validate symbol
            Symbol = input("{}, please pick \"{}\" or \"{}\": ".format(self.Name, Symbols[0], Symbols[1])).upper()  # If symbol is invalid

        self.Sym = Symbol  # If symbol is valid

class Computer:

    def __init__(self):
        self.Name = CPU  # Set computer name to "CPU" constant
        self.Sym = ""  # Initialize the computer's symbol
        self.Score = 0  # Set the score to 0 wins

    def __str__(self):
        return self.Name  # Return computer's name when referenced without properties

    def ValidSquare(self, Squares, Square):
        if Square in Squares and Squares[Square] == " ":  # If the given square exists and is blank
            return True  # Square is valid move

        return False  # Square is invalid move

    def SimulateMove(self, Squares, Symbol, Square):  # Simulate how the board would look after move
        Squares[Square] = Symbol  # Place the player's symbol on the board in the correct square
        return Squares  # Return the layout of the board

    def SimulateWinner(self, Squares, Symbol):  # Simulate a win
        for X, Y, Z in PossibleWins:  # For each square in every possible win
            if Squares[X] == Squares[Y] == Squares[Z] == Symbol:  # If all squares in a row contain the player's symbol
                return True  # The player can win

        return False  # The player can't win

    def RandomMove(self, Squares, MoveList):  # Generate a random move from a given list
        PossibleMoves = []
        for Move in MoveList:  # Create new list from "MoveList" excluding impossible moves
            if self.ValidSquare(Squares, Move):
                PossibleMoves.append(Move)

        if len(PossibleMoves) != 0:
            return random.choice(PossibleMoves)
        else:
            return None

    def ComputerMove(self, Squares, S1):
        for Square in Squares:  # First, check if the computer can win in the next move
            Copy = dict(Squares)
            if self.ValidSquare(Copy, Square):
                self.SimulateMove(Copy, self.Sym, Square)
                if self.SimulateWinner(Copy, self.Sym):
                    return Square

        for Square in Squares:  # Check if the player could win on his next move, and block them
            Copy = dict(Squares)
            if self.ValidSquare(Copy, Square):
                self.SimulateMove(Copy, S1, Square)
                if self.SimulateWinner(Copy, S1):
                    return Square

        Move = self.RandomMove(Squares, ["1", "3", "7", "9"])
        if Move is not None:
            return Move  # Tries to take one of the corners

        if self.ValidSquare(Squares, "5"):
            return "5"  # Tries to take the center

        return self.RandomMove(Squares, ["2", "4", "6", "8"])  # Tries to take one of the sides


# Main
G = Game()  # Create new game
while True:
    G.DisplayBoard()
    G.MakeMove()  # Ask for player's move
    if G.IsWon():  # Check for win
        G.DisplayBoard()
        print("\n{} wins!".format(G.Cur))
        G.DisplayScores()  # Show scoreboard
        if G.IsOver():  # Ask if done playing after game is won
            break  # End game

    elif G.IsDraw():  # Check for draw
        G.DisplayBoard()
        print("\nDraw!")
        G.DisplayScores()  # Show scoreboard
        if G.IsOver():  # Ask if done playing after draw
            break  # End game

    G.SwitchTurn()

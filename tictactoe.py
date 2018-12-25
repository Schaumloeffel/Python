class TicTacToe:
    """
    state stellt den Spielstand als 3x3 Liste dar
    player (0 oder 1) ist der Spieler, der gerade am Zug ist
    """
    
    state = []
    player = 0
    pChars = ['x','O']
    pNames = []
    
    def __init__(self):
        self.state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.player = 0

        self.pNames.append(input("Name Spieler 1: "))
        self.pNames.append(input("Name Spieler 2: "))

    def turn(self):
        inp = self.readInput()
        self.state[inp[0]][inp[1]] = self.pChars[self.player]

        self.printGame()
        
        self.player += 1
        self.player %= 2

    def readInput(self):
        _str = input(self.pNames[self.player] + " ist am Zug: ")
        re = []
        #re = [row,col]
        
        for c in _str:
            if c.isdigit() and len(re) < 2:
                re.append(int(c))

        return re

    def printGame(self):
        print(" _________________")
        print("|     |     |     |")
        print("| ", self.state[0][0] ," | ", self.state[0][1] ," | ", self.state[0][2] ," |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("| ", self.state[1][0] ," | ", self.state[1][1] ," | ", self.state[1][2] ," |")
        print("|_____|_____|_____|")
        print("|     |     |     |")
        print("| ", self.state[2][0] ," | ", self.state[2][1] ," | ", self.state[2][2] ," |")
        print("|_____|_____|_____|")

    def gameOver(self):
        for i in range(0,3):
            if self.state[i][0] == self.state[i][1] and self.state[i][0] == self.state[i][2] and self.state[i][0] != ' ':
                return True
        if self.state[0][0] == self.state[1][1] and self.state[0][0] == self.state[2][2] and self.state[0][0] != ' ':
            return True
        if self.state[0][2] == self.state[1][1] and self.state[0][2] == self.state[2][0] and self.state[0][2] != ' ':
            return True
        return False

_input = input("Neues Spiel: ")

if _input == "":
    game = TicTacToe()

while not game.gameOver():
    game.turn()





        

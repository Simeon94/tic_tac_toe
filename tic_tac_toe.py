from IPython.display import clear_output
# initiating the list of board
board = [" "]*10

#display board function
def displayboard(board):
    clear_output()
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print("--" + "|" + "---" + "|" + "--")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("--" + "|" + "---" + "|" + "--")
    print(f"{board[1]} | {board[2]} | {board[3]}")

#list that contains Signs for Tic-Tac-Toe
signs = ["X","O"]

#creating player class
class Player:
    def __init__(self,name,sign):
        self.name = name
        self.sign = sign
    def __str__(self):
        return "Player Name: " + self.name + " || " + "Symbol: " + self.sign
    def boardinput(self, index, board):
        board[index] = self.sign

#initating playerone
playerone = Player(input("Enter your name: "),input("Choose your sign (X/O): ").upper())

#assigning the other sign to playertwo
if playerone.sign in signs:
    temp = signs[1 - signs.index(playerone.sign)]

#initating playerone
playertwo = Player(input("Enter your name: "),temp)

#board_logic -> return a boolean
def boardlogic(cbd,sign):
    return ((cbd[9]==cbd[6]==cbd[3]==sign)or
    (cbd[7]==cbd[8]==cbd[9]==sign)or
    (cbd[7]==cbd[4]==cbd[1]==sign)or
    (cbd[7]==cbd[5]==cbd[3]==sign)or
    (cbd[4]==cbd[5]==cbd[6]==sign)or
    (cbd[1]==cbd[2]==cbd[3]==sign)or
    (cbd[9]==cbd[5]==cbd[1]==sign)or
    (cbd[8]==cbd[5]==cbd[2]==sign))

#creating a variable -> keeping count of each input
input_count = 0

#GAME_LOGIC_CODE
gameon = True
while gameon:
    #taking playerone input and validating it on the board
    playerone.boardinput(int(input(f"{playerone.name} || Enter index to plot {playerone.sign}: ")),board)
    displayboard(board)
    #checking if the last input of playerone made him the winner
    if boardlogic(board,playerone.sign):
        print(f"{playerone.name} wins!")
        gameon = False
        break
    #checking if the input_counts has exceeded 8 and game draws
    input_count+=1
    if input_count>8:
        print("Game draws!")
        gameon=False
        break
        
    #taking playerone input and validating it on the board
    playertwo.boardinput(int(input(f"{playertwo.name} || Enter index to plot {playertwo.sign}: ")),board)
    displayboard(board)
    #checking if the last input of playerone made him the winner
    if boardlogic(board,playertwo.sign):
        print(f"{playertwo.name} wins!")
        gameon = False
        break
    #checking if the input_counts has exceeded 8 and game draws
    input_count+=1
    if input_count>8:
        print("Game draws!")
        gameon=False
        break
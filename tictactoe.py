import random

board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

current_player = 'x'
winner = None
game_running = True

# Print the game board
def print_box(board):
    """Print the board for the game."""
    print(board[0] + ' | ' + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + ' | ' + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + ' | ' + board[7] + " | " + board[8])

# Take player input
def player_input(board):
    """Take player input."""
    player_input = int(input("Enter a number 1-9: "))
    if player_input >= 1 and player_input <= 9 and board[player_input-1] == "-":
        board[player_input-1] = current_player
    else:
        print("Spot is taken.")
# Check for win or tie
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[2] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[7] != "-":
        winner = board[6]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def check_tie(board):
    """Check for a tie in the board."""
    global game_running
    if "-" not in board:
        print_box(board)
        print("It's a tie!")
        game_running = False

# Switch the player 

def switch_player():
    """Switch players for each turn played."""
    global current_player
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"

def check_win():
    if check_diagonal(board) or check_horizontal(board) or check_row(board):
        print("The winner is {}".format(winner))

# AI 
def tictactoe_AI(board):
    while current_player == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switch_player()

# Check for win or tie again
while game_running:
    print_box(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    tictactoe_AI(board)
    check_win()
    check_tie(board)
import random

board = [" " for _ in range(9)]

def print_board():
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])

def check_win(player):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x in wins:
        if board[x[0]] == board[x[1]] == board[x[2]] == player:
            return True
    return False

while True:
    print_board()
    move = int(input("Enter your move (1-9): ")) - 1
    board[move] = "X"

    if check_win("X"):
        print("You win!")
        break

    ai = random.choice([i for i in range(9) if board[i]==" "])
    board[ai] = "O"

    if check_win("O"):
        print("AI wins!")
        break
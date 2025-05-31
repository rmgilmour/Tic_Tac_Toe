def display_board(board):

    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|\n")
    print("|"," ", board[0][0]," ", "|", " ", board[0][1], " ", "|", " ", board[0][2], " ", "|\n")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|\n")
    print("|"," ", board[1][0]," ", "|", " ", board[1][1], " ", "|", " ", board[1][2], " ", "|\n")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|\n")
    print("|"," ", board[2][0]," ", "|", " ", board[2][1], " ", "|", " ", board[2][2], " ", "|\n")
    print("|"," "*5,"|", " "*5, "|", " "*5, "|")
    print("+","-"*7,"+","-"*7,"+","-"*7,"+", sep="")

def make_list_of_free_fields(board):
    free_nums = []
    free_nums_2d = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'X' or board[i][j] != 'O':
                free_nums.append(board[i][j])
                free_nums_2d = [row[:] for row in board]
    
    free_list = tuple(free_nums)
    print(free_nums_2d)
    print(free_list)

    return free_list


def enter_move(board):
    free = (make_list_of_free_fields(board))
    free_as_list = list(free)

    def inner_func(board,num):
        for x in free_as_list:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        board[i][j] = 'O'

    while True:
        try:
            num = int(input("Select a square:\n"))
            print(num)
            break
        except ValueError:
            print("Incorrect entry. Only enter available numbers 1 through 9. Try again.")
        except EOFError:
            print("Bye Bye.")

    if num not in free_as_list:
        print("That square is taken!")
        num = int(input("Select a square:\n"))
        print(num)
    else:
        inner_func(board,num)

    display_board(board)
    return board


def draw_move(board):
    free = (make_list_of_free_fields(board))
    free_as_draw = list(free)
    from random import randrange
    num = randrange(9)
    print(num)

    def inner_func(board,num):
        for x in free_as_draw:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == num:
                        board[i][j] = 'X'

    while num not in free_as_draw:
        num = randrange(9)
        print("reselected:", num)
        
    inner_func(board,num)

    display_board(board)
    return board
    
def victory_for(board, sign):

    winnerX = ['X', 'X', 'X']
    winnerO = ['O', 'O', 'O']
    
    row1 = [board[0][0],board[0][1],board[0][2]]
    row2 = [board[1][0],board[1][1],board[1][2]]
    row3 = [board[2][0],board[2][1],board[1][2]]
    column1 = [board[0][0],board[1][0],board[2][0]]
    column2 = [board[0][1],board[1][1],board[2][1]]
    column3 = [board[0][2],board[1][2],board[2][2]]
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    diagonal2 = [board[0][2],board[1][1],board[2][0]]
    
    table = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
    
    for i in table:
        if i == winnerX:
            print("I won!")
            exit()
        elif i == winnerO:
            print("You won!")
            exit()
        elif i != winnerX or i != winnerO:
            if sign == 'Z':
                print("it's a tie!")
                exit()
        else:
            print("No winner yet!")
    

board = [[1,2,3], [4,5,6], [7,8,9]]
print("Welcome to Tic Tac Toe!\n")
display_board(board)

counter = 0
while counter < 9:
    
    turn = counter % 2
    if turn != 0:
        print("My turn!")
        draw_move(board)
        if counter >= 5:
            sign = 'X'
            victory_for(board, sign)
    else:
        print("Your turn!")
        enter_move(board)
        sign = 'O'
        if counter >= 5:
            sign = 'O'
            victory_for(board, sign)
    counter += 1
if counter == 9:
    sign = 'Z'
    victory_for(board, sign)

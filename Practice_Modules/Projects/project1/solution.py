import random
test_board = ['#','1','2','3','4','5','6','7','8','9']
board_location = [0,1,2,3,4,5,6,7,8,9]

def print_board(board):
    # print(board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    # print(board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    # print(board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])

    print(f" " + board[7] + " " + '|' + " " + board[8] + " " + '|' + " " + board[9])
    print(f" " + board[4] + " " + '|' + " " + board[5] + " " + '|' + " " + board[6])
    print(f" " + board[1] + " " + '|' + " " + board[2] + " " + '|' + " " + board[3])

def player_input():
    '''
    Output = (player one marker, player two marker)
    '''
    marker = ''

    while (marker != "X" and marker != "O"):
        marker = input("Player 1: Choose X or O: ")

    if (marker == "X"):
        return ('X', 'O')
    else:
        return ('O','X')


# player1_marker , player2_marker = player_input()

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    return ((board[9] == board[8] == board[7] == mark) or
    (board[6] == board[5] == board[4] == mark) or
    (board[3] == board[2] == board[1] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[7] == board[4] == board[1] == mark))


def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
    
    return position

def replay():
    choice = input("Play again? yes or no: ")
    return choice == 'yes'





# place_marker(test_board, '$', 3)
# print_board(test_board)
# print_board(test_board)
# win_check(test_board, "X")


print("welcome to tic-tac-toe")

#While loop to keep running
while True:
    #play the game
    #set everything up(board, who is first, choose markers)
    the_board = [' ']*10

    #player_input() returns a set and will be unpacked
    player1_marker,player2_marker = player_input()

    #Execute function who picks first
    turn = choose_first()

    #print who will go first
    print(turn + ' will go first')

    #Ask users if ready to play.
    play_game = input("Ready to play? y or n?: ")

    #If y, set game_one to True and if not to False
    if play_game == 'y':
        game_on = True
    else: 
        game_on = False
    
    #If game_on set to true play the game, the else statement will take the same functions just switched to player2
    while game_on:
        if turn == 'Player 1':
            #show the board
            print_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place marker
            place_marker(the_board, player1_marker, position)

            #check if won
            if win_check(the_board, player1_marker):
                print_board(the_board)
                print("Player 1 has won!")
                game_on == False
            else: 
                if full_board_check(the_board):
                    print_board(the_board)
                    print("Tie game")
                    game_on = False
                else:
                    turn == 'Player 2'
    
        else:
            #show the board
            print_board(the_board)

            #choose a position
            position = player_choice(the_board)

            #place marker
            place_marker(the_board, player2_marker,position)

            #check if won
            if win_check(the_board, player2_marker):
                print_board(the_board)
                print("Player 2 has won!")
                game_on == False
            else: 
                if full_board_check(the_board):
                    print_board(the_board)
                    print("Tie game")
                    game_on = False
                else:

                    turn == 'Player 1'
    if not replay():
        break


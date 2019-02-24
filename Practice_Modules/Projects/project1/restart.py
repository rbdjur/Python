import string

filled_board = ['#','1','2','3','4','5','6','7','8','9']
board_location = [0,1,2,3,4,5,6,7,8,9]

location_list = []
character_list = []
retry_answers = []
mark_and_num = None
player1_mark = None
player2_mark = None
mark  = ''
num = 0


def print_board(board_list):
    # print(board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    # print(board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    # print(board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])

    print(f" " + board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    print(f" " + board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    print(f" " + board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])

# def input_mark(filled_board, mark):
# def input_mark(filled_board, mark, player1_mark, player2_mark):
def input_mark(filled_board):

   
    mark = input("Hello, player one choose a symbol (X or O): ")

    #If the user (player one) does not choose "O" or "X" as an option, the user will be prompted to enter a response until their response is "O" or "X"
    if (mark != "O" and mark != "X"):
        while (mark != "O" and mark != "X"):
            print("That is not a valid answer. Try again")
            mark = input("Please enter a valid response. O or X: ")


    #user enters correct character, answer is stored as (player1_mark) 
    player1_mark = mark

    #program determines character assignment (player one and player two)

    #player one (player1_mark) chose "X", player2_mark is assigned "O"
    if(player1_mark == "X"):
        player2_mark = "O"

    #if player one chooses "O", then player two will be assigned "X". 
    else:
        player2_mark = "X"

    #print characters for referencing purposes
    print("The character for player one is:", player1_mark)
    print("The character for player one is:", player2_mark)

    # return (mark, player2_mark)
    return (filled_board,player1_mark, player2_mark)



def input_num(filled_board):
# def input_num(filled_board, player1_mark, player2_mark):
# def input_num(filled_board, num, player1_mark, player2_mark):
# def input_num(filled_board, num):


    num = input("Now Player one,please choose a location (1-9) on the number pad:")

    print("This is num before the loop", num)
    print("This is num type before the loop", type(num))

    #Filled board holds the filled board (filled_board[0]), characters of player one (filled_board[1]) and player two (filled_board[2])
    print("This holds the filled_board list and player characters", filled_board)


    #Loop through the filled_board list, and check for correct answer
    for thing in filled_board[0]:
        print("These are the characters in the filled_board list", thing)

        if(num == thing):
            print("The user entered a character (string) that is in filled_board")
            #The input is a string type but is not converted to a int type
            num = int(num)
            print(f"the match is {num} and the type is {type(num)}")

            #Need to pass the user response and the character assignment
            return (num, filled_board)

    #Loop through the filled_board list if answer is not a character in the list.  Redirect handle_input() 

    print("CHECK ME OUT", filled_board[0])

    for thing in filled_board[0]:
        print("This is still our num", num)
        print("thing thing", thing)
        # if(num != thing):
        while(num != thing):
            print("WHY")
            print(f"YERR {num} isn't a valid answer, Redirect")
            ask_again = input("Not a valid answer.  Only numbers (1 through 9 are valid):")

            for hope in filled_board[0]:
                print("This is hope", hope)
                if (ask_again == hope):
                    print("YESSSSSS")
                    num = int(ask_again)
                    # inc = int(ask_again)
                    print(f"this is {num} convert into a {type(num)} under the name of ask_again")
                        
                    return (num, filled_board)
                    # return inc


def handle_input(num, input_num):
    print("Inside handle_input")

    #Confirms access and manpiluation of passed data (num) from input_num function.
    print("lets see what state_two is about", state_two)
    print("This is the type for state_two", type(state_two))

    #State two should either be an int type or a string

    #If state_two is an int type
    if (type(state_two) == type(1)):
        print(f"Passed variable, {state_two}, is a number.")

        if (state_two <= 9):
            print("Valid response")
            print("integer_num is:", state_two)
        else:
            print("Not within range")

        print("Here is the filled_board", filled_board)
        return state_two



def change_marker(filled_board, board_location, inc, state_two):
    print("inside the change_marker function")

    print("This is inc", inc)
    print("This is the filled_board variable", filled_board)
    print("This is the board_location - use this list to link filled board (string representation of number on number pad to the player player to the actual number to change the letter.", board_location)

    #This holds in order in a tuple starting ot [0]: player one's answer, the filled_board list, player one's character, player two's character
    print("This is state_two", state_two)

    print("This should be the list of numbers and the characters of player one and two respectively", state_two[1])

    print("Character of Player one passed from function to function : ", state_two[1][1])
    print("Character of Player two passed from function to function : ", state_two[1][2])

    print("IMPORTANT, this is the location on the board", state_two[0])

    # play_one_char = state_two[1][1]
    # play_two_char = state_two[1][2]

    player1_marker = state_two[1][1]
    player2_marker = state_two[1][2]

    num_loc = state_two[0]

    for xzy in board_location:
        print("location could be ", xzy)
        if (num_loc == xzy):
            print("inside the if statement.")
            print("This is the location on the board", board_location[num_loc])
            print("This is player1_marker", player1_marker)
            filled_board[num_loc] = player1_marker

    print_board(filled_board)

  
    

def win(board_list, mark_and_num):
    print("Inside win function.")
    if (board_list[7] == board_list[8] == board_list[9] == mark_and_num):
        print("Win")

    if (board_list[7] == board_list[4] == board_list[1] == mark_and_num):
        print("Win")

    if (board_list[1] == board_list[2] == board_list[3] == mark_and_num):
        print("Win")

    if (board_list[3] == board_list[6] == board_list[9] == mark_and_num):
        print("Win")

    if (board_list[4] == board_list[5] == board_list[6] == mark_and_num):
        print("Win")

    if (board_list[8] == board_list[5] == board_list[2] == mark_and_num):
        print("Win")

    if (board_list[1] == board_list[5] == board_list[9] == mark_and_num):
        print("Win")
    
    if (board_list[7] == board_list[5] == board_list[3] == mark_and_num):
        print("Win")


print_board(filled_board)


state_one = input_mark(filled_board)

state_two = input_num(state_one)


state_three = handle_input(num, state_two)

change_marker(filled_board, board_location, state_three, state_two)

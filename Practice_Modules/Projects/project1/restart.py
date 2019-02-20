import string

filled_board = ['#','1','2','3','4','5','6','7','8','9']
# filled_board = [0,1,2,3,4,5,6,7,8,9]

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

# def input_mark_num(filled_list, mark, num, player1_mark, player2_mark):
def input_mark_num(filled_board, num, mark):
    # print("Hello Player one, please choose a location (1-9) and symbol (X or O) separated by a space: ")
    # #Ask for user input
    # mark_and_num = input("").split()

    # mark_and_num = input("Hello Player one, please choose a location (1-9) and symbol (X or O) separated by a space:").split()

    # while (mark_and_num != "0" and mark_and_num != "X"):

    mark = input("Hello, player one chose a  symbol (X or O):")

    if (mark != "O" and mark != "X"):
        while (mark != "O" and mark != "X"):
        # mark = input("Hello, player one chose a  symbol (X or O):")
        # if (mark != "O" and mark != "X"):
            print("That is not a valid answer. Try again")
            mark = input("Please enter a valid response. O or X:")
            # mark = input("Hello, player one chose a  symbol (X or O):")
            # print("That is not a valid answer. Try again")

    # print("Here is lowercase letters", string.ascii_lowercase)



    # num = input("Now Player one,please choose a location (1-9) on the number pad:")


    # print("The type of num is",  type(num))

    # print("This is the type of 1", type(1))

    # act_num = int(num)

    num = input("Now Player one,please choose a location (1-9) on the number pad:")

    print("This is num before the loop", num)

    # while(type(num) == type("l")):
    if(type(num) == type("l")):

        while (type(num) != type(1)):
            print("This is a letter. Not a valid response")
            num = input("Please enter a number:")

            for char in filled_board:
                if(num == char):
                    print("The user entered a string that is in filled_board")

                    this_num = int(num)

                    print(f"the match is {this_num} and the type is {type(this_num)}")

                    # return this_num
            
        
    if(type(num) != type(1)):
        for char in filled_board:
            if (num == char):
                print("This is num inside the for loop of filled_board", num)

                print("This is a character in filled_board", char)

                int_num = int(num)

                print(f"The user entered {int_num} of type {type(int_num)}")
                
                print("After match, type of str_num = int", type(int_num))
                break

    integer_num = int(num)

    if (integer_num < 9):
        print("Valid response")
        print("integer_num is:", integer_num)
    else:
        print("Not within range")

    while (integer_num > 9):
        print(f"Your choice of {integer_num} is invalid")
        print("Enter a valid number on the number pad that is 1 through 9")
        num = int(input("Your new selection is:"))
        if (num < 9):
            print(f"Your choice of {num} is a valid answer")
            break

    
    print("This is num", num)
    print("This is mark", mark)

    player1_mark = mark

    if(player1_mark == "X"):
        player2_mark = "O"
    else:
        player2_mark = "X"

    print("player one character is:", player1_mark)
    print("Player two character is:", player2_mark)

    return (mark, num, this_num, player1_mark, player2_mark)

def change_marker(filled_board, l):
# def change_marker(filled_board, l):

    #l is the place holder for:
    # l = input_mark_num()
    #l is our access to all the variables within the input_mark_num() function
    print("inside the change_marker function")

    print("These are all the variables from input_and_num", l)

    board_list = l[0]


    # board_coordinate = int(l[1])
    board_coordinate = l[1]



    player1_marker = l[2]
    player2_marker = l[3]
    # stuff = l[4]

    # print("What will this return?", stuff)    

    print("This is the filled_board variable", board_list)

    # print("This is the player one response", int(player1_marker))

    print("This is the player one response", player1_marker)

    # print("This is the player two response", int(player2_marker))

    print("This is the player two response", player2_marker)

    print("This is the location_list", board_coordinate)

    print("This is filled board", filled_board)

    # for i in range(1,10): 
    #     print("this is i =", i)
    # for num in filled_board[i]:
    # for num in filled_board:
        # print("this is num", num)
        # print("This is filled_board[num] = ", num)
    print("This is board coordinate =", board_coordinate)
            # if (board_coordinate == filled_board[i]):
    if (board_coordinate == 1):
        print("inside the if statement locating the index and switching value to the character marker")
            # for num in filled_board:
        # print("This is an interant of num in filled board", num)
        # if (board_coordinate == num):
        print("the coordinate and the num have linked")
        filled_board[board_coordinate] = player1_marker
    
    if (board_coordinate == 2):
        print("inside the if statement locating the index and switching value to the character marker")
        print("the coordinate and the num have linked")
        filled_board[board_coordinate] = player1_marker

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
# l = input_mark_num(mark_and_num)
l = input_mark_num(filled_board, mark, num)
change_marker(filled_board, l)
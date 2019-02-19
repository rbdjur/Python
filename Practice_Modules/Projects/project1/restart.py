filled_board = ['#','1','2','3','4','5','6','7','8','9']
# filled_board = [0,1,2,3,4,5,6,7,8,9]

location_list = []
character_list = []


def print_board(board_list):
    # print(board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    # print(board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    # print(board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])

    print(f" " + board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    print(f" " + board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    print(f" " + board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])

def input_mark_num():
    print("Hello Player one, please choose a location (1-9) and symbol (X or O) separated by a space: ")
    #Ask for user input
    mark_and_num = input("").split()

    print(mark_and_num)
    print("location", mark_and_num[0])
    print("character", mark_and_num[1])

    #This line may cause bug issues. May need to comment this out
    player1 = mark_and_num[1]

    if (player1 == "X"):
        #line above, may need to replace player1 with mark_and_num[1]
        player2 = "O"
    else:
        player2 = "X"

    print(f"Player one is {player1} and player two is {player2}")
    
    #Put characters inside the list, character_list
    character_list.append(player1)
    character_list.append(player2)

    #Put the number inside location
    location_list = mark_and_num[0]
    #may need to create a location list for user one and user two.
   
    # print_board(filled_board)

    return(filled_board, location_list, player1, player2, character_list)

def change_marker(filled_board, l):
# def change_marker(filled_board, l):

    #l is the place holder for:
    # l = input_mark_num()
    #l is our access to all the variables within the input_mark_num() function
    print("inside the change_marker function")

    # print("These are all the variables from input_and_num", l)

    board_list = l[0]
    board_coordinate = int(l[1])
    player1_marker = l[3]
    player2_marker = l[2]
    stuff = l[4]

    print("What will this return?", stuff)    

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
l = input_mark_num()
change_marker(filled_board, l)
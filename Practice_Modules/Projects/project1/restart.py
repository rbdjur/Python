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

# def input_mark_num(filled_list, mark, num, this_num, player1_mark, player2_mark):
def input_mark(filled_board, mark):
   
    mark = input("Hello, player one choose a symbol (X or O): ")

    if (mark != "O" and mark != "X"):
        while (mark != "O" and mark != "X"):
            print("That is not a valid answer. Try again")
            mark = input("Please enter a valid response. O or X: ")

    # print("This is num", num)
    # print("This is mark", mark)
    # print(f"Player one chose {mark}")

    player1_mark = mark

    if(player1_mark == "X"):
        player2_mark = "O"
    else:
        player2_mark = "X"

    print("The character for player one is:", player1_mark)
    print("The character for player one is:", player2_mark)

    return (mark, player2_mark)


def input_num(filled_board, num):
    num = input("Now Player one,please choose a location (1-9) on the number pad:")

    print("This is num before the loop", num)
    print("This is num type before the loop", type(num))

    for thing in filled_board:
        print(thing)
        if(num == thing):
            print("The user entered a string that is in filled_board")
            # matching_num_filled_board = int(num)
            num = int(num)
            # print(f"the match is {matching_num_filled_board} and the type is {type(matching_num_filled_board)}")
            print(f"the match is {num} and the type is {type(num)}")

            # return matching_num_filled_board
            return num

    for thing in filled_board:
        if(num != thing):
            print(f"{num} isn't a valid answer, Redirect")

            return num

  
# def handle_input(stuff):
# def handle_input(matching_num_filled_board, num):
def handle_input(num):
    print("Inside handle_input")
    print("lets see what this is about", stuff)
    print("This is the type for inc", type(stuff))

    if (type(stuff) == type(1)):
        print("inside the if statement only if inc is a number.")

        print("What is :", stuff)
        print("This is the type of stuff", type(stuff))

        if (stuff < 9):
            print("Valid response")
            print("integer_num is:", stuff)
        else:
            print("Not within range")

        print("Here is the filled_board", filled_board)
        return stuff

    if(type(stuff) == type("l")):
        print("inside the if statement only if inc is a string.")
        
        while(type(stuff) != type(1)):
            ask_again = input("Not a valid answer.  Only numbers (1 through 9 are valid):")
            for thing in filled_board:
                if(ask_again == thing):
                    print("LETS GO")
                    inc = int(ask_again)
                    finally_correct = inc
                    print(f"This is {finally_correct} and the type is {type(finally_correct)}")
                    return inc
                    # break
            



        # return (mark, num, player1_mark, player2_mark)


                                      
    # integer_num = int(num)

    # if (integer_num < 9):
    #     print("Valid response")
    #     print("integer_num is:", integer_num)
    # else:
    #     print("Not within range")

    # while (integer_num > 9):
    #     print(f"Your choice of {integer_num} is invalid.")
    #     print("Enter a valid number on the number pad that is 1 through 9")
    #     num = int(input("Your new selection is:"))
    #     if (num < 9):
    #         print(f"Your choice of {num} is a valid answer")
    #         break

    
    print("This is num", num)
    print("This is mark", mark)

    # print("player one character is:", player1_mark)
    # print("Player two character is:", player2_mark)

    # return (mark, num, this_num, this_diff_num, player1_mark, player2_mark)

    # return (mark, num, this_num, this_diff_num, player1_mark, player2_mark)





    # return (mark, num, this_num, player1_mark, player2_mark)





# def change_marker(filled_board, l):
# def change_marker(filled_board, l):
def change_marker(filled_board, inc, stuff):


    #l is the place holder for:
    # l = input_mark_num()
    #l is our access to all the variables within the input_mark_num() function
    print("inside the change_marker function")

    # print("These are all the variables from input_and_num:", l)

    # board_list = l[0]
    # board_coordinate = l[1]
    # player1_marker = l[2]
    # player2_marker = l[3]

    print("This is inc", inc)
    print("This is the filled_board variable", filled_board)

    # print("This is the filled_board variable", board_list)

    # print("This is the player one response", player1_marker)

    # print("This is the player two response", player2_marker)

    # print("This is the location_list", board_coordinate)

    # print("This is filled board", filled_board)


    # print("This is board coordinate =", board_coordinate)

    # if (board_coordinate == 1):
    #     print("inside the if statement locating the index and switching value to the character marker")
           
    #     print("the coordinate and the num have linked")
    #     filled_board[board_coordinate] = player1_marker
    
    # if (board_coordinate == 2):
    #     print("inside the if statement locating the index and switching value to the character marker")
    #     print("the coordinate and the num have linked")
    #     filled_board[board_coordinate] = player1_marker

    print_board(filled_board)



















# if (board_coordinate == filled_board[i]):









 # for num in filled_board:
        # print("This is an interant of num in filled board", num)
        # if (board_coordinate == num):

















    # board_coordinate = int(l[1])
    # stuff = l[4]

    # print("What will this return?", stuff)    


    # print("This is the player one response", int(player1_marker))



    # print("This is the player two response", int(player2_marker))


    # for i in range(1,10): 
    #     print("this is i =", i)
    # for num in filled_board[i]:
    # for num in filled_board:
        # print("this is num", num)
        # print("This is filled_board[num] = ", num)
  
    

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

# print_board(filled_board)
# l = input_mark_num(mark_and_num)
# l = input_mark_num(filled_board, mark, num, this_diff_num)
# l = input_mark_num(filled_board, mark, num, need_that)
# l = input_mark_num(filled_board, mark, num, this_num, player1_mark, player2_mark)
# l = input_mark_num(filled_board, mark, num, num, player1_mark, player2_mark)
# change_marker(filled_board, l)



print_board(filled_board)
input_mark(filled_board, mark)
stuff = input_num(filled_board,num)
# handle_biz = handle_input(stuff)
# handle_biz = handle_input(matching_num_filled_board, num)
handle_biz = handle_input(num)


# change_marker(handle_biz)
change_marker(filled_board, handle_biz, stuff)

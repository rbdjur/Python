#import function
# from IPython.display import clear_output

#Define global variables
response_one = None
player_one_response = None
player1_marker = None
player2_marker = None

filled_board = ['#','1','2','3','4','5','6','7','8','9']

# location = None

#1. 
#Create a function that takes a list, board_list, as an argument
def print_board(board_list):
    print(board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    print(board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    print(board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])
    # print(f"" + board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    # print(f"" + board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    # print(f"" + board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])
    



#2. Create a function that will take the input of user one and assign characters to player1 and player2
def user_input(response_one, player1_marker, player2_marker):
    #Create a variable with an empty string bc it will eventually hold value
    # response_one = ''

    #Create a while loop that will continue to ask the user to log their character
    while (response_one != "O" and response_one != "X"):
        response_one = input("Player One, please choose your character, X or O: ")

        #create a conditional statement giving a response if the character is not valid
        if (response_one != "O" and response_one != "X"):
            print("That is not a valid answer. Try again.")
        
    
    #Collect the user response and store it in the variable, response_one. 
    player1_marker = response_one

    # Now we can create conditional statements off that response to assign the character of the second player.
    if (player1_marker == "X"):
        player2_marker = "O"
    else:
        player2_marker = "X"

    #sub TROUBLESHOOT
    print(f"Player One chose character {player1_marker}, so Player Two will be {player2_marker}")
    
    return(player1_marker,player2_marker)


#3. Create a function matching the indeces of the list passed to the function, board_list, to integers called , num.
def get_location(board_list, player1_marker, player2_marker):

    player1_marker = player1_marker

    print("CHECK THIS", player1_marker)

    for index in range(1,10):
        location = board_list[index]
        continue
        
    player_one_response = int(input("Player One please choose a number to place your character that corresponds to the location on the number pad: "))

    print(f"Player one chose {player_one_response} for the location")


    change_marker_player_one(player_one_response, board_list,player1_marker)
    #Think about changing the variable passed to change_marker to response to see if the program still runs without errros


    player_two_response = int(input("Player Two please choose a number to place your character that corresponds to the location on the number pad: "))

    print(f"Player two chose {player_two_response} for the location.")

    change_marker_player_two(player_two_response, board_list, player2_marker)



    # numbers = [1,2,3,4,5,6,7,8,9]

    # for num in numbers:
    #     if (player_one_response == num):
    #         print("That is a number on the number pad.")
    #         break

    # sub-TROUBLESHOOT
    # if (player_one == 1):
    #     print("Oh lets do it!")
    #     board_list[1] = "X"
    #     print(board_list)
    # else:
    #     print("That aint it")



    return (player_one_response,location)



#4. Create function that changes the marker on the board
# def change_marker(player_one_response, board_list, location, player1_marker, player2_marker):

# def change_marker_player_one(player1_marker, player_one_response, board_list):
def change_marker_player_one(player_one_response, board_list,player1_marker):
#Think about changing the variable, player_one_response, passed to change_marker to, response, to see if the program still runs without errros
    print("Inside change_marker_player_one")
    print("HEY this is player_one_response", player_one_response)
    print("this is player1_marker", player1_marker)

    if(player_one_response == 1):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker

    if(player_one_response == 2):
        print("inside the if statement")
        # player1_marker = "X"
        # print("this should be X", player1_marker)
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 3):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 4):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 5):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 6):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 7):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 8):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker
    
    if(player_one_response == 9):
        print("inside the if statement")
        # player1_marker = "X"
        print("this should be what player one chose as their character", player1_marker)
        board_list[player_one_response] = player1_marker


    # print("Inside change_marker now for user 2 choice")
    # print("YO this is player_two_response", player_two_response)
    
    # if(player_two_response == 9):
    #     print("inside the if statement")
    #     player2_marker = "O"
    #     print("this should be O", player2_marker)
    #     board_list[player_two_response] = player2_marker
    print("updated board")
    print_board(board_list)



def change_marker_player_two(player_two_response, board_list, player2_marker):
#Think about changing the variable, player_one_response, passed to change_marker to, response, to see if the program still runs without errros
    print("Inside change_marker_player_two")
    print("HEY this is player_one_response", player_two_response)

    if(player_two_response == 1):
        print("inside the if statement")
        # player2_marker = "O"
        print("this should be what player one chose as their character", player2_marker)
        # print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 2):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 3):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 4):
        print("inside the if statement")
        # player2_marker = "O"
        print("this should be what player one chose as their character", player2_marker)
        # print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 5):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 6):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 7):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker
    
    if(player_two_response == 8):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker

    if(player_two_response == 9):
        print("inside the if statement")
        player2_marker = "O"
        print("this should be O", player2_marker)
        board_list[player_two_response] = player2_marker
    
    print("updated board")
    print_board(board_list)


#Collect smaller functions into this function
def main_function(response_one, player1_marker, player2_marker, player_one_response, filled_board):


# def main_function():

#Think about changing the variable, response_one, passed to change_marker to, response, to see if the program still runs without errros
    user_input(response_one, player1_marker,player2_marker)
    print_board(filled_board)
    l = get_location(filled_board, player1_marker, player2_marker)
# change_marker(player_one_response, filled_board, location, player1_marker, player2_marker)
    change_marker_player_one(filled_board, player1_marker, l)
    change_marker_player_two(filled_board, player2_marker, l)


#DRIVER CODE
main_function(response_one, player1_marker, player1_marker, player_one_response, filled_board)

    

        





#TROUBLESHOOT
#test printing the board
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# print_board(test_board)


#1 TROUBLESHOOTING
# filled_board = ['#','1A','2B','3C','4D','5E','6F','7G','8H','9I']
# print_board(filled_board)




#2 TROUBLESHOOTING
# beginning = user_input()
# print(beginning)

#3 TROUBLESHOOTING
# empty_board = ['','','','','','','','','','']
# filled_board = ['#','1','2','3','4','5','6','7','8','9']
# match_index(empty_board)
# print_board(empty_board)



  # board_list[1] = 1
    # board_list[2] = 2
    # board_list[3] = 3
    # board_list[4] = 4
    # board_list[5] = 5
    # board_list[6] = 6
    # board_list[7] = 7
    # board_list[8] = 8
    # board_list[9] = 9
#import function
# from IPython.display import clear_output

#1. 
#Create a function that takes a list, board_list, as an argument
def print_board(board_list):
    # #Prompt Player One to pick a character
    # user_input()

    #print the indeces of the passed list, board_list, with pipe character |' separating each index.  Place the indeces in rows of 3
 
    print(board_list[7] + " " + '|' + " " + board_list[8] + " " + '|' + " " + board_list[9])
    print(board_list[4] + " " + '|' + " " + board_list[5] + " " + '|' + " " + board_list[6])
    print(board_list[1] + " " + '|' + " " + board_list[2] + " " + '|' + " " + board_list[3])



#2. Create a function that will take the input of user one and assign characters to player1 and player2
def user_input():
    #Create a variable with an empty string bc it will eventually hold value
    response_one = ''

    #Create a while loop that will continue to ask the user to log their character
    while (response_one != "O" and response_one != "X"):
        response_one = input("Player One, please choose your character, X or O: ")

        #create a conditional statement giving a response if the character is not valid
        if (response_one != "O" and response_one != "X"):
            print("That is not a valid answer. Try again.")
        
    #sub - TROUBLESHOOT
    # print(f"Player one chose character {response}")
    
    #Once the user logs their response and it is stored in the variable, response. Now we can create conditional statements off that response to assign the character of the second player.
    player1_marker = response_one
    # player2 = ' '
    if (player1_marker == "X"):
        player2_marker = "O"
    else:
        player2_marker = "X"

    #sub TROUBLESHOOT
    print(f"Player One chose character {player1_marker}, so Player Two will be {player2_marker}")
    
    return(player1_marker,player2_marker)

#3. Create a function that matches the indeces of the list passed to the function, board_list, to integers called , num.

def get_location(board_list):
    for index in range(1,10):
        location = board_list[index]
        
    player_one_response = int(input("Player One please choose a number to place your character that corresponds to the location on the number pad: "))

    print("You chose for location the number:", player_one_response)

    numbers = [1,2,3,4,5,6,7,8,9]

    for num in numbers:
        if (player_one_response == num):
            print("That is a number on the number pad.")
            break

    # sub-TROUBLESHOOT
    # if (player_one == 1):
    #     print("Oh lets do it!")
    #     board_list[1] = "X"
    #     print(board_list)
    # else:
    #     print("That aint it")

    print_board(board_list)

    return (player_one_response,location)

    

    
    

    

#RUNNING CODE
user_input()
filled_board = ['#','1','2','3','4','5','6','7','8','9']
print_board(filled_board)
get_location(filled_board)
    

        





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
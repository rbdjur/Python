#import function
# from IPython.display import clear_output

#1. 
#Create a function that takes a list, board_list, as an argument
def print_board(board_list):
    #Prompt Player One to pick a character
    user_input()

    #print the indeces of the passed list, board_list, with pipe character |' separating each index.  Place the indeces in rows of 3
    print(board_list[7] + '|' + board_list[8] + '|' + board_list[9])
    print(board_list[4] + '|' + board_list[5] + '|' + board_list[6])
    print(board_list[1] + '|' + board_list[2] + '|' + board_list[3])

    #Once the board is displayed, the indeces will be assigned to integer values to gain access to changing the character in the corresponding number pad location. 
    match_index(board_list)


#2. Create a function that will take the input of user one and assign characters to player1 and player2
def user_input():
    #Create a variable with an empty string bc it will eventually hold value
    response = ''

    #Create a while loop that will continue to ask the user to log their character
    while (response != "O" and response != "X"):
        response = input("Player one, please choose your character, X or O: ")

        #create a conditional statement giving a response if the character is not valid
        if (response != "O" and response != "X"):
            print("That is not a valid answer. Try again.")

    #sub - TROUBLESHOOT
    # print(f"Player one chose character {response}")
    
    #Once the user logs their response and it is stored in the variable, response. Now we can create conditional statements off that response to assign the character of the second player.
    player1 = response
    # player2 = ' '
    if (player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"

    #sub TROUBLESHOOT
    print(f"Player One chose character {response}, so Player Two will be {player2}")
    
    return(player1,player2)

#3. Create a function that matches the indeces of the list passed to the function, board_list, to integers called , num.

def match_index(board_list):
      for index in range(1,10):
        # for num in range(1,3):
        location = board_list[index]
        print("This is the number", index)
        print("These are the values of the indeces", location)
    

    # sub-TROUBLESHOOT
    

        





#TROUBLESHOOT
#test printing the board
# test_board = ['#','X','O','X','O','X','O','X','O','X']
# print_board(test_board)


#1 TROUBLESHOOTING
filled_board = ['#','1A','2B','3C','4D','5E','6F','7G','8H','9I']
print_board(filled_board)




#2 TROUBLESHOOTING
# beginning = user_input()
# print(beginning)

#3 TROUBLESHOOTING
# empty_board = ['','','','','','','','','','']
# filled_board = ['#','1','2','3','4','5','6','7','8','9']
# match_index(empty_board)
# print_board(empty_board)






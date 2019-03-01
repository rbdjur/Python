#The try block will execute and examine the code in this block
try:
    result = 10 + 10
    print(result)
except:
    #if the code contains an error, the code in the except block will execute
    print("Adding is not happening check type")



#The try block will execute and examine the code in this block

try:
    # add = 5 + '5'
    add = 5 + 5
    print(add)
except:
    #if the code contains an error, the code in the except block will execute
    print("adding is not happening.")
else:
    #If the code is clean and has no errors, then this code will run
    print(add)
    print("Went well.")
finally:
    #This code runs regardless if there is an error or not
    print("Thee End")
    
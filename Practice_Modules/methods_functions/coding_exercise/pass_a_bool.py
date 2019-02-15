#Pass one argument to the function
def inside_outside(a):
    #If the argument is true, print message back notifying inside the function
    if (a):
        print("inside function")
    else:
    #If not not, print message saying outside the function (never entered)
        print("outside")

inside_outside(False)
inside_outside(True)
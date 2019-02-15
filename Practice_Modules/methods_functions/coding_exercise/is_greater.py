#pass two arguments to the function
def is_greater(a,b):
    #If the first argument is greater than the second argument, return True
    if(a>b):
        return True
    #If the first argument is less than or equal to the second argument, return False
    elif (a <= b):
        return False

greater = is_greater(5,4)
lesser = is_greater(1,2)

print(greater)
print(lesser)
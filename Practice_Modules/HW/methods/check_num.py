#define a function that takes three arguments, num, low, high.
def num_check(num,low,high):
    #If the number is greater than or equal to low AND number is less than or equal to high
    if (num >= low and num <= high):
        return True
    #If num does not fulfill these conditions
    else:
        return False

number = num_check(28,1,10)
print(number)

#Success
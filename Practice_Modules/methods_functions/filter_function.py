def check_even(num):
    #Checks if num is an even number
    return num % 2 == 0

mynums = [1,2,3,4,5,6]

#Filter returns True or False.
#filter applies the condition of the check_even function to the mynums list.
print(filter(check_even,mynums))
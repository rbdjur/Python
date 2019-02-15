#Pass *args keyword to the function for an arbitrary number of arguments.
def my_func(*args):
    #declare a list variable, my list, and use list comprehension to return the arguments passed by the user if the number is an even number
    mylist = [num for num in args if num % 2 ==0]
    return mylist

evens = my_func(1,2,3,4,5,6,7,8,9,10)
print(evens)

def square_num(x):
    return x**2

mylist = [1, 2, 3, 4, 5]

#When using map. The first argument is the function you want to use, and the second argument is the thing you want to pass to the function.

#When passing the function name as the first argument, you do not nee to include the parentheses.
new_result = map(square_num,mylist)
print(new_result)
#This above will just return the address of where this information is stored

#return values of mylist passed to square_num, in a list
list_version = list(map(square_num,mylist))
print(list_version)

 
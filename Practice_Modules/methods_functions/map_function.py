def square_num(x):
    return x * x

mylist = [1, 2, 3, 4, 5]

new_result = map(square_num,mylist)
print(new_result)
#This above will just return the address of where this information is stored

#return values in a list
list_version = list(map(square_num,mylist))
print(list_version)


# def myfunc(*args):
#     return sum(args) * 2

# double = myfunc(1,2,3,4,5,6,7,8,9,10)

# print(double)



# def afunc (**kwargs):
#     if 'fruit' in kwargs:
#         print("My favorite fruit is {}".format(kwargs['fruit']))
#     else:
#         print("I did not find any fruit")
    
#     print(kwargs)


# my_stuff = afunc(fruit='apple', veggie='lettuce')

def bfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))

bfunc(10,20,30,food="eggs", fruit="orange", animal="dog")

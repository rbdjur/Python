#The use of '*args' allows us to set an arbitrary amount of arguments and returns a tuple.

def myfunc(*args):
    return sum(args) * 2

double = myfunc(1,2,3,4,5,6,7,8,9,10)

print(double)


# '**kwargs' does the same thing as *args except instead of return the arguments in a tuple, they are returned as a dictionary
def afunc (**kwargs):
    if 'fruit' in kwargs:
        print("My favorite fruit is {}".format(kwargs['fruit']))
    else:
        print("I did not find any fruit")
    
    print(kwargs)

print("Thank u next", afunc(fruit='apple', veggie='lettuce'))

# my_stuff = afunc(fruit='apple', veggie='lettuce')

# We can use '*args' and '**kwargs' in combination by passing both of them to the function in the beginning.
def bfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print("I would like {} {}".format(args[0], kwargs['food']))

bfunc(10,20,30,food="eggs", fruit="orange", animal="dog")

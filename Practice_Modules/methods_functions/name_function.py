def name_function():
    print("Hello")

# name_function()

#prints out hello to terminal when program ran.

def say_hello(name):
    return 'Hello ' + name

result = say_hello("You")
print(result)

# print(result)

def add(n1, n2):
    #Figure out why if I uncomment the line directly below invokes a incorrect syntax error.
    # print(f'You entered two variables {} {}'.format(n1,n2)
    return n1+n2

result = add(20,30)
print(result)


# find out if the word "dog" is in a string
def dog_in(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False

#This will return false
check = dog_in('Hello friends')
print(check)



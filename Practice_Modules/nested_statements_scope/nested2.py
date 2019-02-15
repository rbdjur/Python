x = 25

def func():
    global x
    print(f'X is {x}')

    #Local reassignment on a global variable
    x = 'New Value'
    print(f'X is now {x}')

func()
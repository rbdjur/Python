#one.py

#define a function called, func, that prints out to terminal that - this is Func in one.py
def func():
    print("Func() in one.py".upper())

#level one message to terminal
print("TOP LEVEL IN ONE.PY")

#Msg saying if the code is run direclty print inside if statement, if not run directly print inside else.
if __name__ == '__main__':
    print("One.py is being run directly!".upper())
else:
    print("One.py has been imported.".upper())
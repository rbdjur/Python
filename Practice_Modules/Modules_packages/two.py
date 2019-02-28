#imports one.py and runs all the code at the 0 level of indentation
import one

#print msg to terminal
print("top level in two.py")

#executes the function, func(), in one.py that is represented by one.
one.func()

#Msg saying if the code is run direclty print inside if statement, if not run directly print inside else.
if __name__ == '__main__':
    print("Two.py is being run direclty.".lower())
else:
    print("One.py is imported.".lower())
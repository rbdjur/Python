#Create a function that takes three arguments.  If z is true, return x. If z if False, return y
def myfunc(x,y,z):
    if(z):
        return x
    else:
        return y

which = myfunc("YUP!", "NOPE!", True)
print(which)

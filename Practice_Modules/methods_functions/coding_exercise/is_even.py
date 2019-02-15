#pass an argument to the function.
def is_even(a):
    #If the number passed to the function is an even number return true
    if (a % 2 ==0):
        return True
    else: 
        #If not, return false
        return False

even = is_even(2)
odd = is_even(3)

print("This is even variable", even)
print("This is odd variable", odd)
try:
    x = 5
    y = 0
    z = x / y
except:
    print("Cannot divide by 0")
    x = 5 
    y = 1
    z = x / y 
    print('But you can divide by 1, the answer is', z)
finally:
    print("All done.")
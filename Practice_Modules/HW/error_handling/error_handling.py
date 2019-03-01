try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("Cannot square strings")
    for i in [1,2,3]:
        print(f"The number is {i}")
        print(f"This is the integer squared however, {i**2}")
        


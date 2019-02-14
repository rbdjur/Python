mystring = 'Hello'
mylist = []

#1 way
# for letter in mystring:
#     mylist.append(letter)
#     print(letter)

#2 way

#This way below puts each letter into an index in the list
mylist = [letter for letter in mystring]
print(mylist)

#This below puts a number into an index for as many numbers in the list, mylist2
mylist2 = [num for num in range(0,10)]
print(mylist2)

#This belows puts only even numbers in an index for as many numbers in the num_list list
num_list = [num for num in range(0,10) if num % 2 == 0]
print(num_list)

#tempertature conversion from celsius into fahrenheit

celsius = [0, 10, 20, 34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celsius]

print(fahrenheit)
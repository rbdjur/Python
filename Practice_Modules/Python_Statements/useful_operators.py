#import a library
from random import shuffle
from random import randint

#shuffles the list into random order
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
#The list printed should be shuffled into random order.
print("this is the shuffle(list)", mylist)

#randint returns a random integer between two passed arguments.
print("This is a randint", randint(0,10))

#to save a random integer we can assign randint() to a variable
save_me = randint(0,11000)
print("This is saving a randomly generated number.", save_me)



#use of the range function
#This operation prints numbers from 0 to 10, in crements of 2. So 2,4,6,8,10.
for num in range(0,11,2):
    print(num)

#use of the enumerate function
word = 'abcde'

#returns a tuple with an index count assigned to each item of the variable you are iterating through.
for item in enumerate(word):
    print(item)

#zip function
mylist = [100,200,300]
mylist2 = ['a', 'b', 'c']
mylist3 = ["square", "circle", "triangle"]

#Zipping a list matches a corresponding index to another list, when you iterate through a zip(), the corresponding matching indexes will print together.
zip(mylist, mylist2)

for item in zip(mylist, mylist2, mylist3):
    print(item)

#in operator
#returns true if the given item (number or string) is in a list, dict, etc.
print(2 in [1,2,3])

#min function returns back the minimum of the object passed.
mylist = [10,20,30,40,100]
minimum = min(mylist)
print(minimum)
#max function returns back the maximum of the object passed.
maximum = max(mylist)
print(maximum)

#input function accepts user input.
#This allows you to pass a string to give instructions, immediately allowing the user to type input back.
#Note that when you use the input function, whatever is typed and entered is always a string
result = float(input("Enter a number here: "))
print("The number you entered is: ", result)

#to convert the input using input() into a different datatype...
#This will convert result from a string to a float
print(type(result))
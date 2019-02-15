#To add letters from an interable variable into a list.
mystring = 'WHAT???'
#This is a shortcut way to add elements one by one into a list
mylist = [letter for letter in mystring]
print(mylist)

#add multiples of 5 into a list
stuff = [x for x in range(0,100,5)]
print(stuff)

#print only the even numbers from 0 to 20
my_evens = [even for even in range(0,21) if even % 2 ==0]
print(my_evens)

#print only the odd numbers from 0 to 20
my_odds = [odd for odd in range(0,21) if odd % 2 == 1]
print(my_odds)

#print all even numbers and print blue for all odd numbers 0-10
#          variable, condition              range
numbers =[num if num % 2 ==0 else 'blue' for num in range(0,11)]
print(numbers)

#nested loops
#mylist = []

#for x in [2, 4, 6]
    #for y in [1, 10, 1000]
        #mylist.append(x*y)

#multiplies 2 by 1, 10, 1000.  Multiples 4 by 1, 10, 1000. Multiplies 6 by 1, 10, 1000

#Use list comprehensions to represent above example
        #operation, #variable in list, #another variable in list
list_comp=[x*y for x in [2,4,6] for y in [1, 10, 1000]]
print(list_comp)

#success

#notes:
#element for element in an_iterable_object

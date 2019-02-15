#Create a list that holds 3 strings
my_list = ['one', 'two', 'three']

#Create a list that holds 2 strings.
another_list = ['four', 'five']

print(my_list)
print(another_list)

#concatentate the two lists
new_list = my_list + another_list

print(new_list)

#lets change the 0th index to read 'All CAPS'.  
new_list[0] = 'ALL CAPS'

print(new_list)

#add element at end of list
new_list.append('six')
print(new_list)

#Remove the last item of new_list
new_list.pop()
print(new_list)

#remove a specific index pass in the position of the index.
#remove the third item in the list 
new_list.pop(2)
print(new_list)

#Use the .sort() method that puts the list in alphabetical order.
letters_list = ['a', 'g', 'e', 'n', 'c', 'y']
print(letters_list)

#The letters are not in alphabetical order.
letters_list.sort()
print(letters_list)

#An unordered list of numbers
num_list = [ 4, 1, 3, 0, 6, 2]
print(num_list)
#Order the num_list
num_list.sort()
print(num_list)

#Put the numbers in reverse order
num_list.reverse()
print(num_list)
#Success


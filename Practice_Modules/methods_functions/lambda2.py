names = ['Andrew', 'Akash', 'Kaz']

#print the first letter of each item in the list, arrays
#the first name after lambda, is the iterant variable name for the list
#name[0] refers to the first letter of the name
#,names is the object list that stores these items.
print(list(map(lambda name: name[0], names)))

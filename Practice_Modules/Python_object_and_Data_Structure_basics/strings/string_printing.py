#.format{} method
# Whatever is inside of format() is plugged in wherever there are a curly braces, palceholders, in the string
print("this is a string {}".format("Inserted"))

# The numbers inside the curly braces correspond to the order of the indeces of the arguments passed to format().
print("The {2} {1} {0}".format("fox", "brown", "quick"))
#This will print "the quick brown fox"

print('The {q} {b} {f}'.format(f="fox", b="brown", q="quick"))

#f-string method
#declare a variable, name and set it to a name
name = 'brian'

#print the name brian.

#the f-string method uses the print() function.
#inside the print function if a, f.
#Allows you to write variables directlu into string using string interpolation concept.
print(f'The person goes by {name}')
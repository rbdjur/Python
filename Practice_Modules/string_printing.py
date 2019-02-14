# Whatever is inside of format() is plugged in wherever there is a curly braces in the string
print("this is a string {}".format("Inserted"))

# The numbers inside the curly braces correspond to the order of the indeces of the arguments passed to format().
print("The {2} {1} {0}".format("fox", "brown", "quick"))
#This will print "the quick brown fox"

print('The {q} {b} {f}'.format(f="fox", b="brown", q="quick"))
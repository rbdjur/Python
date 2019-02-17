# Create a function that takes a list
# Thelist = []
def unique(Thelist):
    # pass Thelist through the set function and assign it to variable new.
    new = set(Thelist)
    #pass new to list to pass the new variable as a list to be returned
    return list(new)

#Example1
vUnique = unique([1,1,2,2,3,4,5,6,6,7,8,8])
print(vUnique)

#Example2
sUnique = unique([1,1,1,1,1])
print(sUnique)

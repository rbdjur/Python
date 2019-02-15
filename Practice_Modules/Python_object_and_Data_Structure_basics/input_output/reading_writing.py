#second argument of open: mode='r', reads the file.

#w = write
#a = append to file.
#r+ = reading and writing
#w = is writing and reading (overwrites existing files or makes a new one)

#with this method of opening a file in this syntax, you do not need to explicitly close the file.
#reads to the file
with open('new_file.txt', mode='r') as f:
    contents = f.read()
    print(contents)

#a appends text to a file at the end of the file.
with open('new_file.txt', mode = 'a') as f:
    f.write('\nFour on Fourth')

with open('new_file.txt', mode='r') as f:
    contents = f.read()
    print(contents)

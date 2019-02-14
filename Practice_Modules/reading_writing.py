#second argument of open: mode='r', reads the file.

#w = write
#a = append to file.
#r+ = reading and writing
#w = is writing and reading (overwrites existing files or makes a new one)
with open('new_file.txt', mode='r') as f:
    contents = f.read()
    print(contents)

with open('new_file.txt', mode = 'a') as f:
    f.write('\nFour on Fourth')

with open('new_file.txt', mode='r') as f:
    contents = f.read()
    print(contents)

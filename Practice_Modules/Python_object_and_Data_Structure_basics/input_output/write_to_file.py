# %%writefile text.txt
# I am writing this text via write_to_file.py

#Opens the text.txt file
myfile = open('text.txt')

#reads the file and prints the contents of the file to the console.  Note, the cursor of the text.txt file is at the end of the file.
print(myfile.read())

#reset the cursor back to the beginning of the file in case you want to read the file again.
myfile.seek(0)

#place reading the file into contents
contents = myfile.read()

#print contents
print(contents)

#set the cursor of the file back to the beginning
myfile.seek(0)

#readlines() returns the text in a list.  Each line break or line of the file is created as its own item in the list.  Check terminal for results.
print(myfile.readlines())

#close the text.txt file
myfile.close()
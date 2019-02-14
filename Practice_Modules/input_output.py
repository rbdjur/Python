# myfile = open('text.txt')
# # print(myfile.readline())

# #read myfile
# print(myfile.read())
# myfile.seek(0)

with open('text.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)




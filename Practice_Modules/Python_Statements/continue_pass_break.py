x = [1, 2, 3]

for item in x:
    #Does nothing at all
    pass

print('end of my script')

mystring = 'name'

for letter in mystring:
    if letter == 'a':
        #continue goes back to the top of the loop. So the result will read n, m, e
        continue
    print(letter)


mystring2 = 'Where'

for letter in mystring2:
    if letter == 'e':
        #break stops the code if the letter is 'e'.  So the result will be 'W' and 'h'
        break
    print(letter)

#Success
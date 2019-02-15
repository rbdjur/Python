def myfunc(mystring):
    #Create a variable that holds an empty string.
    string = ''

    #use the enumerate function to assign an index, i, to each letter,letter in the string.
    for i,letter in enumerate(mystring):
        if i % 2 ==0:
            #If the index is an even index, then use the .upper() method on the letter and add it to the empty string variable, string
            string += letter.upper()
        else:
            #The alternate action for the above if statement, is to add the lowercase letter to the string
            string += letter

    return string

word = myfunc("mississippi")
print(word)
#create a function that takes a string
def palindrome(string):
    #set the string to the variable, word
    word = string
    #Use a condition statement stating if the word is equal to the word in reverse (palindrome)
    if(word == word[::-1]):
        return True
    else:
        return False

success = palindrome("racecar")
print(success)

failure = palindrome("today")
print(failure)

#Success
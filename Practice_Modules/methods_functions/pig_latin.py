def pig_latin(word):
    first_letter = word[0]

    if (first_letter in 'aeiuo'):
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    
    return pig_word


word = pig_latin('apple')
print(word)
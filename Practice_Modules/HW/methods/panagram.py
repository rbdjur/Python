#import string
import string
alphabet = string.ascii_lowercase

def panagram(thestring, alphabet):
    new_new = set(thestring)
    for letter in new_new:
        # print(letter.lower())
        if (letter == alphabet):
            print("We made it")
            return True
        else: 
            return False
    
    # for letter in new_new:
    #     if (letter == al):
    #         return True
    #         # continue
    #     else:
    #         continue
        # return True



    # return set(string)
    # for letter in string:
    #     if(letter == alphabet):
    #         continue
    #     else:
    #         return False
    #     return True

# panagram("The quick brown fox jumps over the lazy dog", alphabet = string.ascii_lowercase)



word = panagram("who is at the door?", alphabet)
print(word)

second_example = panagram("The quick brown fox jumps over the lazy dog", alphabet)
print(second_example)
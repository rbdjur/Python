def check(mystring):
    empty_string = ''
    lower_count = 0
    upper_count = 0

    for letter in mystring:
        empty_string += letter
    
    for some in empty_string:
        if (some == ' '):
            continue
        elif (some == some.upper()):
            upper_count += 1
        elif (some == some.lower()):
            lower_count += 1
        
    print("there amount of upper case letters are ", upper_count)
    print("There amount of lower case letters are ", lower_count)
    
check('WHAT IS THE DEAL')

#Success
def multiply_list(Thelist):
    #Declare output assigned to 1 and as a global variable
    output = 1
    for num in Thelist:
        #Loop through the num in Thelist
        output *= num
        # print(output)
    return output
    

product = multiply_list([1,2,3,4])
print(product)

#1

# st = 'print only the words that start with s in this sentence'

# new_list = st.split()
# print(new_list)

# for item in new_list:
#     first_letter_index = 0 
#     if(item[first_letter_index] == 's'):
#         print(item)

#2

# for num in range(0,11):
#     if (num % 2 == 0):
#         print(num)

#3

# num_50 = [num for num in range(0,51) if num % 3 == 0]

# print(num_50)

#4
# st = 'print every word in this sentence that has an even number of letters'

# new_st = st.split()

# for word in new_st:
#     if(len(word) % 2 == 0):
#         print("The {word} is even", word)

#5
# for num in range(1,101):
#     if (num % 3 == 0) & (num % 5 ==0):
#         print("FizzBoom")
#     elif (num % 5 == 0):
#         print("Boom")
#     elif (num % 3 == 0):
#         print("Fizz")
#     else:
#         print(num)

#6
st = 'Create a list of the first letters of every word in this string'

new_st = st.split()

new_result = [letter[0] for letter in new_st if letter[0]]

print(new_result)





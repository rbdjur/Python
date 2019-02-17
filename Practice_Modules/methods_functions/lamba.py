#a lambda expression is a function that will be used only one time
# def square(num):
#     result = num ** 2
#     return result

#This is the lambda expression.  'num' is the passed argument to the function.  Return is removed because it is assumed you want to return the expression of the lambda function.

mynums = [1,2,3,4,5,6]
lambda num: num **2

#prints a list of the numbers inside, mynums, squared.  The use of the map() passes the lmbda function as its first argument, and the list of numbers as the second argument.
print(list(map(lambda num:num **2, mynums)))

#prints values of the list of only the even numbers based on set of conditions of True or False
print(list(filter(lambda num:num % 2 ==0, mynums)))


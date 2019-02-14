#define 3 lists of various items
mylist1 = ['a','b','c']
mylist2 = [1,2,3]
mylist3 = ['circle', 'triangle', 'square']

#loop through each item of zip'd list and print item.
for item in zip(mylist1,mylist2,mylist3):
    print(item)

# loop through each variable of zip'd list and print item. Print only the numbers
# for a,b,c in zip(mylist1,mylist2,mylist3):
#     print(b)


#put each zip'd list into a list
print(list(zip(mylist1,mylist2,mylist3)))


#success
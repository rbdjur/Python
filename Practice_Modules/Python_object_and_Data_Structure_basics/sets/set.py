myset = set()

#add number 1 to set
myset.add(1)

print(myset)

#add number 2 to the set
myset.add(2)

#add number 2 again to the set
myset.add(2)

#see what the results of a set are
print(myset)

#Only {1,2} are in set despite adding two 2's.  this is because a set only holds unique values.  IF the value already exists, it wont take another number that is already identical to the number in the set.
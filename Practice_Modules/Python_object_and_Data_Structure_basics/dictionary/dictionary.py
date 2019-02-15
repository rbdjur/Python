my_dict = {'key 1':'value 1', 'key2': 'value2'}

print(my_dict)

prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk': 5.80}
#lets print out the price of apple
print(prices_lookup['apple'])

d = {'k1':123, 'k2':[0,1,2], 'k3': {'insidekey': 100}}

#lets print the list
print(d['k2'])

#lets print the dictionary
print(d['k3'])

#lets print the value only k3
print(d['k3']['insidekey'])

#lets print 2 from the list of 2 in d
print(d['k2'][2])

#change value of k1 to "New Value"
d['k1'] = 'New Value'
print(d)

#Print only the keys of the values
print(d.keys())

#Print only the values of the values
print(d.values())

#print the keys and values
print(d.items())
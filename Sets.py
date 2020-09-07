# Sets in python 
# a set is a unordered collection of data type 
# it is iterable 
# we use curly braces in set {}

set1 = {1,2,3,4,4,4,4,4,4,4,4,}
#print(set1)  # the set will not let repeat the value

# to add values in the set
# we use .add function for that 
# for example

#set1.add(222)
#print(set1)

# and when to add multiple values we will use .update function 

set1.update([22,11,23,3,4,5,6,7,8,9,9.76,5,54,4],["tom"])
#print(set1)

# to remove 
# we use .remove function 
# for example 

#set1.remove(22)
#print(set1)

# to clear all the set we will use .clear function
#set1.clear()  # clear will remove all the values from the set 
#print(set1)

# .discard function this is a linenit function to remove a value it does not show the error if a value is not in a set 
# for example 

set1.discard("Harrp potter ")
print(set1)

# we can use .pop, .del, .remove and many other functions which we use on the tuple,  list 
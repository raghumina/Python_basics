# INDEXES 
# the list  contains several numbers. Print the third number from this list.
#You don't have to handle the input.
#Sample Input 1:
#[5230, 5661, 5081, 9539, 5563]
#Sample Output 1:
# 5081

# One way 
numbers = [5230, 5661, 5081, 9539, 5563]
third_element = numbers[-3]
print(third_element)

# another way
numbers = ['5230', '5661', '5081', '9539', '5563']
#third_element = numbers[-3]
print(numbers[-3])

# one more way
numbers = [5230, 5661, 5081, 9539, 5563]
#third_element = numbers[-3]
print(numbers[2])


# 2nd Problem
# We have created a variable for the lowercase English alphabet:
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# Your task is to print the 15th letter of this string.
alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[-12])

# Problem 3 

#Find the initial letter of a person's name and print it out.
#Make use of the variable name that stores a string.
#Sample Input 1:
#Kate
#Sample Output 1:
#K
#Sample Input 2:
#Ivor
#Sample Output 2:
#I

name = "Kate"
print(name[-len(name)])

name = "Ivor"
k = name[0]
print(k)

# Problem 4 

#Sentences generally end with a certain punctuation mark: a period ., an exclamation point !, or a question mark ?.
#Find out which of these symbols marks the end of a string stored in the variable sentence and print it out.
#Sample Input 1:
#What a lovely day!
#Sample Output 1:
#!

sentence = "What a lovely day!"
print(sentence[-1])

# Problem 5

# Modify the list numbers so that each number in it coincides with its index (not the negative one). In the end, print the list.

numbers = [4, 1, 0, 3, 2, 5]  # This is also the given list 
index = numbers.index(4, 1, 0, 3, 2, 5)
print(index)
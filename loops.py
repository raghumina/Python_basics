# loops in python 
# 

# lets print numbers from 1 to 1000
# so lets start 
'''
for i in range(0,1001):
    print(i)
'''
'''
# lets use this on a list 
list1 = ["Tom", 22,33,4,45,5,6]
for items in list1:           # it will print the all the values in the list 
    print(items)

# lets try something else 
# 

dict1 = {
    "name": "tom",
    "class": 4,
    "roll no": 5,
    "sunject": "maths "
}

for data in dict1:
    print(data, dict1[data])  # this will show the data not the keys 

'''
# lets do this for tuples 

tup1 = ("1",2,3,4,5,6,7)
for i in tup1:
    print(i)
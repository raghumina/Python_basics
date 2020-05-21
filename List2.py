# updating a list 
# adding values to the list 

guest = ['tom','alex','tim','mateo','rex']
print(guest[0])  # the output will be tom 

# adding more string to guest list 
guest[0] = 'Yoda'
print(guest[0])  # now the output will be yoda 

# creating a list with arguments 
def greet(msg):
    print("hello",guest[1],msg,"enjoy oyur day")
greet("good morning")    

# we can also add value to the list with append()
# add anew value to the end of the list 
guest.append("roger")
print(guest[-1])  # i will get the roger as a output 

# how to remove a name from the list 
# will use .remove for this 
# for example 
guest.remove("roger")
print(guest[-1])  # this time the output will be rex

# another command for this is del
del guest[-1]
print(guest[-1])  # and this time our output is mateo 

# one more command to add or update string or variable to string 
# the list = ['tom','alex','tim','mateo','rex']
guest[3] = 'tiko'
print(guest[3])  # the output will be tiko instead of mateo


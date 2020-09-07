# type casting with different different variables 
##a = "Tom "
##b = 22 
##print(a + b)
# this will show a error in it 
# now i will use the type casting 
# type casting is changing one data type to another 

##a = "tom"
##b = str(22)
##print(a + b) 
'''
# now it wil show a output tom22

# lets check another example 
# lets try to make a simple program  with type casting method 

# the idea is to print a number woith type casting 
num1 = 22 
num2 = "22"
print(num1 + int(num2))  # this also works like this 


# lets take another simple problem 
a = 22 
b = "22"
c = 22.22
print(type(a))
print(type(b))
print(type(c))

a = 22 
a = str(a)
print(type(a))

b = "22"
b = int(b)
print(type(b))

c = 22.22
c = str(c)
print(type(c))



# strip functions in python 
# strip 
# the strip function will remove the excess space in the variable 
# and the r strip will remove the space from the right side of the variable 
# and as usual the lstrip will remove the space from the left side of the variable 

name  = "    tom    "
print(name.strip())

# and the len function 
# the len finction is used to find the length of the varaible 
title = "Harry Potter and Prisoner of Azkaban"
print(len(title))  # it gives a length of 36 , it also counts the spaces between the words 

print(title.upper()) # converts all the variable in upper case 
print(title.lower())  # converts all the varaible in lower case 

# replace function 
# this function will replace the given value with another given value 
# for example 

Name = "Tom and Perry"
Name1 = Name.replace("P","J")
print(Name1)



# to interchange the variables 
player1 = "Messi"
player2 = "Ozil"
line = f"{player1} is better than {player2}"
print(line)
'''
# lets use this on multiple lines 
player1 = "messi"
player2 = "neymar"
player3 = "suarez"

msn = f"msn is the greastest football attacking trident in which{player1} palyes as RW, and {player2} playes as LW, and {player3} palyes as CF among this three the {player1}is the best player"
print(msn)
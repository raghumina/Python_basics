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
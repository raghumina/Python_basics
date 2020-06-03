# and & or in python 
# the and condition runs only when both the give conditions are true 
name = input("please Enter your name ")
section = input("Please enter your section ")
if name == "Xyz" and section == "a":
    print("you can view your marks ") 
elif name == "qwe" or section == "a,b,c":
    print("please confirm your self ")
else:
    print("Please check your respective class")


# another example 
# largest number among three numbers 
print("please enter numbers")
print("enter number 1")
num1 = int(input())
print("enter number 2")
num2 = int(input())
print("enter number 3")
num3 = int(input())
if num1 >= num2 and num1 >= num3:
    print("num1 is the largest number ")
elif num2 >= num1 and num2 >= num3:
    print("num2 is largest number")
else:
    print("number3 is the largest number ")    


# we can combine and or in one line to get the desired output 
# this makes python more user friendly

# for example 
print("Please enter your name")
name = input()
print("please enter your code")
code = input()
print("please enter your id")
id = int(input())
print("please enter ypur department name")
dept = input()
if name == "XYZ" and code == "qwe" and id == "001"\
    or dept =="computer":
    print("welcome back ")
else:
    print("please enter your details again")
    print("or login in your own system")


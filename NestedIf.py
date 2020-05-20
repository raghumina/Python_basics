# Nestedif in python 
# we can use if in if means more conditions in a condition 
# work same as normal condition 
print("please enter your details")
print("Please enter your name ")
name = input()
print("please enter your code ")
code = input()
print("please enter your id ")
id = int(input())
print("please enter your department")
dept = input()
if name == "Xyz":
    print("go to next step")
    if code == "qwe":
        print("good ")
        if id == "001":
            print("very good")
            if dept == "computer":
                print(""" woww
                welcomebacl""")

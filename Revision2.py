# Revison 2 
# conditional statements 

# # # a basic program using if 
# print("Please enter the price")
# price = int(input())
# if price > 1000:
#     print("out of range ")
# if price < 1000:
#     print("In range ")


# another condition using for 

for i in range(5):  # completes the loop until it finishes its range 
    print(i)
    if i < 3 :
        print("its ohk ")


# Nested if 
number = 1002
if number > 1001 :
    print("num is greater\n")   
    if number < 1003:
        print("num is small\n")
        if number > 100:
            print("number is so big\n")
            if number < 10000:
                print("number is so smaller\n")
                if number > 1:
                    print("number is so so big\n ")
                    if number < 100000:
                        print("number is so smaller\n")
print("thats all for now ")    


# if esle 
num = 100 
if num < 1000:
    print("\n smaller")
else:
    print("bigger")    
print("got your answer ")


# if , else , elif
x = 10 
if x < 5:
    print("bigger")
elif x > 12 and x < 10:
    print(" what is this ")
else:
    print("save me from this comples logic")  # no upper condition will be true so this message will get printed 
print("that\'s all")   



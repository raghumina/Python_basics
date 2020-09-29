# This is a program to guess a number 
# 

number = 10
chances = 0 
while chances <=4:
    user_input = int(input("Enter your guess: "))
    chances = chances + 1 
    if user_input == number:
        print("you won !!!!")
   

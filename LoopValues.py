# how to access loop values 
# loop values in python 

# for steps in range(1,4,5):
#     print("steps")

import turtle 
for steps in ['green','red','blue','yellow']:
    turtle.color(steps)
    turtle.forward(100)
    turtle.right(90)
    for steps1 in['yellow','red','grey','blue','black']:
        turtle.color(steps1)
        turtle.forward(210)
        turtle.right(120)
        

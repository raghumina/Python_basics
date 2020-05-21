# while loops 
# while loop alllow you to execute unyil a particul condition is true 
# a = "4"
# while a = "4":
#      print("yes 2 + 2 = 4")

import turtle
counter = 0
while counter < 4:  # it will repeat the loop for 4 time until it got a true condition 
      turtle.forward(100)
      turtle.right(90)
      counter = counter+1  # if we will convert + to - it will become a infinite loop because condition will never completed. 
      for steps in range (100):
          turtle.color("green")
          turtle.forward(120)
          turtle.right(140)

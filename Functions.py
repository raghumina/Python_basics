# # functions in python 
# # they help to make a program simple and short 
# # we can assign a task in function 


#  def printMsg():   # Defining a function "printMsg"
#      print("hello Team")  # Inside the function 
#      return  # this wil help to exit the function 

# #   # here we are calling the function 
# #             # the output will be "hello Ronaldo" bcz thats what we defined in a functuon 

# # # lets create a new function 

# def main():
#     printMsg()   # our old fuction in the new function 
#     printPlayers()  # a new function we have created 
#     return

# def printPlayers():
#     printPlayers = ["Messi","Ronaldo","Kaka","Zidane","Tom"]
#     for printPlayers in printPlayers:
#         print(printPlayers)
#     return


# main()


# lets try a one more function 

import turtle 

def lines():
    turtle.forward(100)
    turtle.right(90)
    for lines in range(8):
        turtle.color("red")
        turtle.forward(100)
        turtle.right(90)
    return    

# main()
lines()
lines()
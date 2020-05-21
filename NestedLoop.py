# we use the nested loop with turtle 

# import turtle
# for steps in range(4):
#     turtle.color('red')
#     turtle.forward(100)
#     turtle.right(90)
#     for steps1 in range(4):
#         turtle.color('green')
#         turtle.forward(50)
#         turtle.right(90)
#         for steps2 in range(10):
#             turtle.color('blue')
#             turtle.forward(30)
#             turtle.right(90)


# lets try to make a octagon
# import turtle
# for steps in range(100):
#     turtle.color('blue')
#     turtle.forward(100)
#     turtle.right(45)


# we can use numbers to decide how many side our structure will have 

import turtle
sides = 6  # we have choose the number of sides 
for steps in range(sides):
    turtle.color('blue')
    turtle.forward(100)
    turtle.right(360/sides)
    for steps1 in range(sides):
        turtle.forward(50)
        turtle.right(180/sides)
        for steps2 in range(sides):
            turtle.forward(50)
            turtle.right(180/sides)
            for steps3 in range(sides):
                turtle.forward(70)
                turtle.right(360/sides)
                for steps4 in range(sides):
                    turtle.forward(100)
                    turtle.right(90/sides)





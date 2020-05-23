# import turtle
# counter = 0
# While counter <= 6:
# 	Turtle.forward(100)
# 	Counter += 1
import turtle

for steps in range(5):	
	turtle.forward(100)
	turtle.right(90)
	for moresteps in rage(4):
		turtle.forward(50)
		turtle.right(90)


a = 1
b = 2
c = 3
d = 4
e = 5
if ((a == 1 and
     b == 2 and
     c == 4) or
     (d == 4  and e == 5)):
    print("Yeah, Working")
else:
    print("ooops")
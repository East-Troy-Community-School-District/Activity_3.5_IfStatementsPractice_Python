'''
Color Shapes
1/9/2023
Python I
'''

import turtle

t = turtle.Turtle()

shape = input("What shape do you want to see? >> ")
turtleColor = input("What color do you want the shape? >> ")

# Changes the color of the turtle, if valid
if turtleColor == "red":
    t.color("red")
elif turtleColor == "blue":
    t.color("blue")
# Add your code here!
else:
    print("Invalid color!")

# Draws the selected shape, if valid
if shape == "square":
    side = int(input("How big should the sides be? >> "))
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
elif shape == "circle":
    radius = int(input("How big should the radius be? >> "))
    t.circle(radius)
# Add your code here!
else:
    print("Invalid shape!")

'''
Color Shapes
Pawelski
10/15/2023
Introduction to Computer Science
'''

import turtle
import time

t = turtle.Turtle()
t.hideturtle()


# Gets and changes the color of the turtle, if valid
turtleColor = turtle.textinput("Color", "What color do you want the shape?")

if turtleColor == "red":
    t.color("red")
elif turtleColor == "blue":
    t.color("blue")
# Add your code here!
else:
    t.write("Invalid color!", align="center", font=("Arial", 60))
    time.sleep(5)
    exit()


# Gets and draws the selected shape, if valid
shape = turtle.textinput("Shape", "What shape do you want to see?")

if shape == "square":
    side = turtle.numinput("Side Length",
                           "What is the side length of the square?")
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
elif shape == "circle":
    radius = turtle.numinput("Radius",
                             "What should the radius of the circle be?")
    t.circle(radius)
# Add your code here!
else:
    t.write("Invalid shape!", align="center", font=("Arial", 60))
    time.sleep(5)
    exit()

turtle.mainloop()
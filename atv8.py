import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(10)

colors = ['purple', 'blue', 'yellow', 'green', 'pink', "black", "red"]
for _ in range (10):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(90)
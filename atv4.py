import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(10)
colors = ["green" , 'purple', 'blue', "pink", "black"]

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)  
    turtle.right(360)
    turtle.forward(100)
    turtle.left(120)
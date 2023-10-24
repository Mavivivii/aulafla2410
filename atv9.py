import turtle
import random

turtle = turtle.Turtle()

turtle.pensize(4)

colors = ["purple", "blue", "yellow", "red"]
for c in range(360):
      color = random.choice(colors)           
      turtle.color(colors)
      turtle.forward(1)
      turtle.right(1)
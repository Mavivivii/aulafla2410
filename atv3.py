import turtle 
turtle = turtle.Turtle() 


turtle.pensize(23) 

turtle.shape("turtle") 


for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)


for color in ['blue', 'black', 'red', 'pink']:
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)


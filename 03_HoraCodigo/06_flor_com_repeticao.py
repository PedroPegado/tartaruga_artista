import turtle

turtle = turtle.Turtle()

for c in range(12):
    for _ in range(2):
        turtle.forward(60)
        turtle.left(30)
        turtle.forward(60)
        turtle.left(150)
    turtle.left(30)
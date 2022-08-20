import turtle

turtle = turtle.Turtle()
# definindo as funções
def desenhe_forma():
    for _ in range(6):
        turtle.forward(25)
        turtle.right(60)

def pule(pixels):
    turtle.penup()
    turtle.forward(pixels)
    turtle.pendown()


# Aqui é o código principal
for _ in range(6):
    for _ in range(2):
        for _ in range(4):
            desenhe_forma()
            pule(75)
        pule(-25)
        turtle.right(60)
        pule(25)
        turtle.right(120)
    pule(-25)
    turtle.left(60)
    pule(50)
    turtle.right(60)
import turtle

turtle = turtle.Turtle()

# definindo a função
def desenhe_uma_flor():
    for _ in range(6):
        for _ in range(8):
            turtle.forward(20)
            turtle.right(30)
        turtle.right(60)


# chamando a função (apenas na chamada que a função é executada)
turtle.penup()
turtle.backward(150)
turtle.pendown()
desenhe_uma_flor()
turtle.penup()
turtle.fd(150)
turtle.pendown()
desenhe_uma_flor()
turtle.penup()
turtle.fd(150)
turtle.pendown()
desenhe_uma_flor()

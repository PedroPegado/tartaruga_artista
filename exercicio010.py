"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.color('red')
    turtle.shape('circle')
    turtle.forward(100)
    turtle.right(90)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()

for _ in range(4):
   turtle.color('blue')
   turtle.shape('arrow')
   turtle.right(90)
   turtle.forward(100)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

for _ in range(4):
   turtle.color('green')
   turtle.shape('square')
   turtle.forward(100)
   turtle.right(90)

turtle.penup()
turtle.goto(100, 200)
turtle.pendown()

for _ in range(4):
   turtle.color('yellow')
   turtle.shape('turtle')
   turtle.right(90)
   turtle.forward(100)

turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()

for _ in range(4):
   turtle.color('black')
   turtle.shape('classic')
   turtle.forward(500)
   turtle.right(90)
   


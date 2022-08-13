"""
Exercícios

1) Mude a ordem das cores
2) Mude/defina a forma da tartaruga
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.pensize(10)
turtle.shape('arrow')

for color in ['red', 'blue', 'pink', 'black']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)
turtle.forward(100)
for color in ['red', 'blue', 'pink', 'black']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)


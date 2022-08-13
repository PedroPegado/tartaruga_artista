"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random

turtle = turtle.Turtle()
colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'orange', 'black', 'pink', 'light blue']
turtle.speed(0)

for c in range(360):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(3)
    turtle.right(1)

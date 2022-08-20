from turtle import *

def go(x, y):
  penup()
  goto(x, y)
  pendown()

def square(tam, lado):
  begin_fill()
  for c in range(4):
    fd(tam)
    lado(90)
  end_fill()

def rect(tam1, tam2, lado):
  begin_fill()
  for c in range(2):
    fd(tam1)
    lado(90)
    fd(tam2)
    lado(90)
  end_fill()

hideturtle()
go(-50, -175)
speed(0)

#sapato steve
color('#848486')
left(90)

rect(30, 80, right)

#calça steve
penup()
fd(31)
color('#5749D2')
pendown()

rect(110, 60, right)

go(10, -144)
rect(100, 10, right)

go(20, -144)
rect(90, 10, right)

#camisa steve
color('#01DFE3')
go(-50, -34)
rect(120, 60, right)

go(10, -44)
rect(130, 10, right)

go(20, -54)
rect(140, 10, right)

go(-50, 46)
square(40, left)

go(30, 46)
square(40, right)


#bracos steve
color('#D79E81')
right(180)
go(31, 46)
rect(100, 39, left)

go(-51, -54)
right(180)
rect(100, 39, left)

#cabeca steve
go(-50, 87)

square(80, right)

#cabelo steve
color('#191007')

go(-50, 147)
rect(20, 80, right)

right(180)
square(10, left)

go(20, 137)
right(180)

square(10, right)
right(90)

#partes rosto steve
go(-39, 127)
#olhos
color('white')
square(10, right)
go(9, 127)
square(10, right)

color('#6A50B5')
go(-28, 127)
square(10, right)
go(-2, 127)
square(10, right)

color('#B3624F')
go(-18, 107)
rect(16, 10, right)

#barba
color('#55260C')
go(-28, 97)
rect(36, 9, right)

go(-28, 107)
square(10, right)
go(-2, 107)
square(10, right)

#nariz
go(-18, 117)
color('#8A533F')
rect(16, 9, right)

#sombra calça 
go(0, -104)
color('#473DAE')
rect(20, 10, right)

go(-40, -104)
rect(20, 10, right)

go(8, -46)
square(10, right)
go(0, -36)
square(10, right)

#sombra bracos
color('#BC8C75')
go(-71, -53)
rect(20, 10, left)
go(-71, -44)
square(10, left)
go(-90, -53)
square(10, left)
go(-61, 7)
rect(10, 30, right)
go(-81, 27)
rect(10, 20, right)

go(31, -53)
rect(20, 10, left)
go(41, -44)
square(10, left)
go(31, 7)
rect(10, 30, right)
go(49, 27)
rect(10, 20, right)

#pescoco steve
color('#D69E83')
go(-28, 87)
rect(36, 10, right)
go(-19, 77)
rect(20, 10, right)

#sombras camisa
color('#00c2c2')
go(-49.5, -24)
rect(30, 10, right)
go(-20, 6)
rect(10, 30, right)
go(-49.5, 46)
rect(10, 40, right)
go(-39.5, 46)
rect(10, 20, right)
go(20, 46)
rect(10, 100, right)
go(10, 46)
square(10, right)
go(-9, 66)
rect(10, 50, right)
go(-19, 66)
rect(10, 20, right)
go(-61, 78)
square(10, right)
go(-61, 57.5)
square(10, right)
go(-90.5, 86)
square(10, right)
go(-90.5, 57.5)
square(10, right)
go(31, 78)
square(10, right)
go(31, 57.5)
square(10, right)
go(60.5, 86)
square(10, right)
go(60.5, 57.5)
square(10, right)

#sombras camisa 2
color('#00d5d9')
go(-9, 16)
rect(10, 30, right)
go(50.5, 86)
rect(10, 20, right)
go(-80.5, 86)
rect(10, 20, right)
go(-90.5, 67.5)
square(10, right)
go(60.5, 67.5)
square(10, right)
go(10, 36)
rect(10, 40, right)
go(-39, 86)
square(10, right)
go(10, 86)
square(10, right)

#bloco esquerda mines
color('#765338')
go(-80, 186)
left(20)
square(20, right)
color('#64A43A')
right(90)
rect(5, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(10, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(7.5, 5, left)
left(90)
fd(5)
right(90)
rect(10, 5, left)
left(90)
fd(5)
right(90)
rect(5, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(10, 2.5, left)

#bloco direita mines
color('#765338')
go(45, 190)
right(310)
square(20, right)
color('#64A43A')
right(90)
rect(5, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(10, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(7.5, 5, left)
left(90)
fd(5)
right(90)
rect(10, 5, left)
left(90)
fd(5)
right(90)
rect(5, 2.5, left)
left(90)
fd(2.5)
right(90)
rect(10, 2.5, left)

#nome minecraft

#LETRA M 
go(-350, 175)
left(110)
color('black', '#AEA4A2')
begin_fill()
fd(20)
right(90)
fd(10)
left(90)
fd(10)
right(90)
fd(10)
left(90)
fd(20)
left(90)
fd(10)
right(90)
fd(10)
left(90)
fd(10)
right(90)
fd(20)
right(90)
fd(70)
right(90)
fd(20)
right(90)
fd(40)
left(90)
fd(10)
left(90)
fd(20)
right(90)
fd(20)
right(90)
fd(20)
left(90)
fd(10)
left(90)
fd(40)
right(90)
fd(20)
right(90)
fd(70)
end_fill()

#LETRA I
go(-260, 175)
right(90)
rect(20, 70, right)

#LETRA N
go(-230, 175)
begin_fill()
fd(20)
right(90)
fd(10)
left(90)
fd(10)
right(90)
fd(15)
left(90)
fd(10)
left(90)
fd(25)
right(90)
fd(20)
right(90)
fd(70)
right(90)
fd(20)
right(90)
fd(25)
left(90)
fd(10)
right(90)
fd(15)
left(90)
fd(10)
left(90)
fd(40)
right(90)
fd(20)
right(90)
fd(70)
end_fill()

#LETRA E
go(-160, 175)
begin_fill()
right(180)
fd(70)
left(90)
fd(50)
left(90)
fd(15)
left(90)
fd(30)
right(90)
fd(12.5)
right(90)
fd(30)
left(90)
fd(15)
left(90)
fd(30)
right(90)
fd(12.5)
right(90)
fd(30)
left(90)
fd(15)
left(90)
fd(50)
end_fill()

#LETRA C
go(90, 175)
begin_fill()
right(180)
fd(50)
right(90)
fd(15)
right(90)
fd(30)
left(90)
fd(40)
left(90)
fd(30)
right(90)
fd(15)
right(90)
fd(50)
right(90)
fd(70)
end_fill()

#LETRA R 
go(150, 175)
right(90)
begin_fill()
fd(50)
right(90)
fd(25)
right(90)
fd(10)
left(90)
fd(10)
left(90)
fd(10)
right(90)
fd(35)
right(90)
fd(20)
right(90)
fd(25)
left(90)
fd(10)
left(90)
fd(25)
right(90)
fd(20)
right(90)
fd(70)
end_fill()
go(170, 145)
color('black')
rect(20, 10, right)

#LETRA A
right(90)
go(210, 175)
color('black', '#AEA4A2')
begin_fill()
fd(50)
right(90)
fd(70)
right(90)
fd(20)
right(90)
fd(20)
left(90)
fd(10)
left(90)
fd(20)
right(90)
fd(20)
right(90)
fd(70)
end_fill()

go(225, 135)
color('black')
rect(10, 5, right)

go(230, 140)
square(10, right)

go(240, 135)
rect(10, 5, right)

go(240, 150)
square(10, right)

go(220, 150)
square(10, right)

#LETRA F
go(270, 175)
color('black', '#AEA4A2')
begin_fill()
right(180)
fd(70)
left(90)
fd(20)
left(90)
fd(27.5)
right(90)
fd(30)
left(90)
fd(15)
left(90)
fd(30)
right(90)
fd(12.5)
right(90)
fd(30)
left(90)
fd(15)
left(90)
fd(50)
end_fill()

#LETRA T
go(330, 175)
begin_fill()
right(180)
fd(50)
right(90)
fd(20)
right(90)
fd(15)
left(90)
fd(50)
right(90)
fd(20)
right(90)
fd(50)
left(90)
fd(15)
right(90)
fd(20)
end_fill()
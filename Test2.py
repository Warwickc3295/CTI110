import turtle
turtle.speed(10)
turtle.color('hotpink')
turtle.bgcolor('red')
turtle.pensize(2)
size=1

while (True):
    for x in range(4):
          turtle.forward(size)
          turtle.right(60)
          size=size + 1
    turtle.right(10)

# CTI-110
# M5LAB - Turtle Lab
# Cameron Warwick
# 10/9/17

def main():
    import turtle
    for x in range(4):
        turtle.forward(64)
        turtle.left(90)
    turtle.penup()
    turtle.forward(128)
    turtle.pendown()
    for y in range(3):
        turtle.forward(64)
        turtle.left(120)
main()




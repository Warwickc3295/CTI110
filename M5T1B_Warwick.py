# CTI-110
# M5LAB - Turtle Lab
# Cameron Warwick
# 10/11/17

def main():
    import turtle
    turtle.bgcolor('lightgreen')
    turtle.color('blue')
    turtle.pensize(5)
    
    # C shape
    
    turtle.right(180)
    turtle.forward(32)
    for x in range(9):
        turtle.left(20)
        turtle.forward(32)

    # Switching
        
    turtle.forward(20)
    turtle.penup()
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(180)
    turtle.pendown()

    # W shape

    turtle.right(160)
    turtle.forward(180)
    turtle.left(140)
    turtle.forward(180)
    turtle.right(140)
    turtle.forward(180)
    turtle.left(140)
    turtle.forward(180)





main()
    

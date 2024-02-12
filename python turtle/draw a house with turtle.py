import turtle

def triangle():                                      #draw the triangle bit of the house
    turtle.left(90)
    turtle.forward(500)
    turtle.right(90)
    for line in range(3):
        turtle.forward(500)
        turtle.left(120)

def door():                                      #draw the door of the house
    turtle.setpos(100, -450)
    for lines in range(2):
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(150)
        turtle.left(90)
    turtle.setpos(0, -450)


def squares(square_length, position, position2):
    turtle.penup()
    turtle.setpos(position, position2)
    turtle.pendown()
    for lines in range(4):
        turtle.forward(square_length)
        turtle.left(90)

turtle.setpos(0, -450)
squares(500, 0, -450)
door()
triangle()
squares(100, 300, -279)
squares(100, 300, -100)
squares(100, 100, -100)
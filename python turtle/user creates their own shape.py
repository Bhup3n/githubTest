import turtle

def shape(num_side, colours, pen_width):
    turtle.pensize(pen_width)
    turtle.pencolor(colours)
    user_angle = 360 / num_side
    for line in range(num_side):
        turtle.forward(100)
        turtle.right(user_angle)

num_sides = int(input("how many sides should there be:"))
colour = input("what colour should it be:")
width = int(input("what should be the width of the pen:"))

shape(num_sides, colour, width)
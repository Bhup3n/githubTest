import turtle

turtle.pensize(20)
turtle.penup()
turtle.setpos(-200, 200)
turtle.pendown()
for line in range(0,5):
    turtle.pencolor("blue")
    turtle.forward(100)
    turtle.left(72)

turtle.penup()
turtle.setpos(200,200)
turtle.pencolor("red")
turtle.pendown()
turtle.forward(100)
turtle.hideturtle()
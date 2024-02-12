from tkinter import *
import time
from Ball import *       #imports everthing from the ball class we made in the python file called Ball

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volleyball = Ball(canvas, 0, 0, 100, 1, 1, "blue") #this is us passing in arguments to the function in the class in the other file
tennisball = Ball(canvas, 0, 0, 50, 4, 3, "green")  #create a new ball
football = Ball(canvas, 0, 0, 120, 2, 4, "black")
basketball = Ball(canvas, 0, 0, 140, 5, 8, "orange")

while True:
    volleyball.move()        #calls the move function in the other file
    tennisball.move()
    football.move()
    basketball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
from tkinter import *
import time


class Square:

    def __init__(self, canvas, x1, y1, x2, y2, x_velocity, y_velocity, colour):
        self.canvas = canvas
        self.image = canvas.create_rectangle(x1, y1, x2, y2, fill=colour)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

    def move(self):
        coords = self.canvas.coords(self.image)     #get coords of the rectangle
        #this gives us 4 coordinates, first 2 are for top left corner and the x and y coord and the next 2 are the bottom right x and y coordinate

        if coords[2] >= self.canvas.winfo_width() or coords[0] < 0:  #if bottom right x coordinate is bigger than or equal to the canvas' width or the top left x coordinate is less than 0:
            self.x_velocity = -self.x_velocity     #change the horizontal direction to the opposite

        if coords [3] >= self.canvas.winfo_height() or coords[1] < 0: #if bottom right y coordinate is bigger than or equal to the canvas' height or the top left y coordinate is less than 0:
            self.y_velocity = -self.y_velocity    #change the vertical direction to the opposite

        self.canvas.move(self.image, self.x_velocity, self.y_velocity)     #moves ball at whatever the x velocity and y velocity is at



window = Tk()

WIDTH = 1000
HEIGHT = 1000   #creating constant variables

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

square1 = Square(canvas, 250,250,300,300, 3, 4, "red")
square2 = Square(canvas, 250,250,300,300, 5, 4, "orange")
square3 = Square(canvas, 250,250,300,300, 2, 4, "yellow")
square4 = Square(canvas, 250,250,300,300, 8, 5, "green")      #calling the square class
square5 = Square(canvas, 250,250,300,300, 1, 2, "blue")
square6 = Square(canvas, 250,250,300,300, 9, 6, "purple")
square7 = Square(canvas, 250,250,300,300, 6, 2, "black")

while True:
    square1.move()
    square2.move()
    square3.move()     #uses move function from the class we created
    square4.move()
    square5.move()
    square6.move()
    square7.move()
    window.update()
    time.sleep(0.01)

window.mainloop()

#NOTE:  we would usually put the class and the window codes in seperate files and import the class code into the window code using from (filename) import *
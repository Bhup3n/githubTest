from tkinter import *
import time

WIDTH = 500       #these are called constants which are things you dont plan on changing. we are using this because we will use this a few times
HEIGHT = 500      #they're names are in capitals because that is how we normally name them, it isnt necessary though
x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

back_image = PhotoImage(file="photos/space.png")
background = canvas.create_image(0,0,image=back_image, anchor=NW)

myimage = PhotoImage(file="photos/dog.png")
image = canvas.create_image(0,0,image=myimage, anchor=NW)

image_width = myimage.width()           #figures out width and height of our image
image_height = myimage.height()

while True:      #keeps on running until we close program,  if we make a game, we would usually use while running which means until you close out of the game
    coords = canvas.coords(image)    #get the coords of where image is located

    if coords[0] >= (WIDTH - image_width) or coords[0] < 0:      #if our coordinates at [elemnt 0] (which means x coordinate) is greater than or equal to our width or if our x coordinate is less than 0, the following code will execute...   the WIDTH - image_width is so that it goes the opposite direction when the first pixel of the image touches the right border whereas before it wouldnt
        x_velocity = -x_velocity                 #this will turn our x velocity to the negative version of it which means it will reverse the direction

    if coords[1] >= (HEIGHT - image_height) or coords[1] < 0:      #does the same thing but for the y coordinates
        y_velocity = -y_velocity

    canvas.move(image, x_velocity, y_velocity)        #moves our image by the amount of pixels on the x axis and the amount of pixels on the y axxis
    window.update()       #updates window for any changes made
    time.sleep(0.01)      #thread sleeps for 0.1 seconds, the lower the number, the faster the GUI (with tkinter) window runs

window.mainloop()
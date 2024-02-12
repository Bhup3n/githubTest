from tkinter import *
import time

WIDTH = 1700
HEIGHT = 1000
x_velocity = 8         #how fast ball goes horizontally
y_velocity = 7          #how fast ball goes vertically
racket1_collision = False   #if racket 1 is colliding
racket2_collision = False   #if racket 2 is colliding
ball_exit = True       #has the ball left the screem
score = 0     #a score to see how long the ralley was

def up_rack1(event):
    canvas.move(racket1, 0, -100)

def down_rack1(event):
    canvas.move(racket1, 0, 100)

def up_rack2(event):
    canvas.move(racket2, 0, -100)

def down_rack2(event):
    canvas.move(racket2, 0, 100)


window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

racket1 = canvas.create_rectangle(20, 20, 100, 250, fill="blue")
racket2 = canvas.create_rectangle(1680, 980, 1600, 750, fill="red")

window.bind("<w>", up_rack1)
window.bind("<s>", down_rack1)
window.bind("<Up>", up_rack2)
window.bind("<Down>", down_rack2)

ball = canvas.create_oval(650, 650, 690, 690, fill="black")


while True:
    coords = canvas.coords(ball)
    ball_width = coords[2] - coords[0]     #figures out the ball width
    ball_height = coords[3] - coords[1]    #figures out the ball height
    overlap = canvas.find_overlapping(*coords) #finds if something overlaps something else, we use *coords because we can then give it however many arguments we want

    if racket1 in overlap:    #if racket 1 is in overlapping, this means the ball is colliding with the racket and the following code happens
        x_velocity = -x_velocity   #then reverse the horizontal direction
        racket1_collision = True   #racket 1 did collide
        racket2_collision = False    #racket 2 didnt
        score += 1    #adds plus one to the score

    elif racket2 in overlap:
        x_velocity = -x_velocity
        racket2_collision = True    #racket 2 did collide
        racket1_collision = False   #racket 1 didnt
        score += 1

    else:
        racket1_collision = False    #racket 1 didnt collide
        racket2_collision = False    #racket 2 didnt collide


    if coords[0] >= (WIDTH - ball_width) or coords[0] < 0:      #if x coordinate of ball touches the border on the left or right
        if ball_exit == True:
            end_label = Label(canvas, text="The ball has gone off", font=("Arial", 40, "bold"), fg="black")    #tells the user the ball has gone off
            end_label.pack()
            score_label = Label(canvas, text="your final score was " + str(score), font=("Arial", 45, "bold"), fg="black")   #shows user final score
            score_label.pack()
            ball_exit = False      #just setting it back to false so the labels dont keep on spamming themselves

    if coords[1] >= (HEIGHT - ball_height) or coords[1] < 0:     #if y coordinate of ball touches top or down border
        y_velocity = -y_velocity

    canvas.move(ball, x_velocity, y_velocity)
    window.update()         #this is needed so the canvas actually displays and the window keeps on updating every 0.01 seconds
    time.sleep(0.01)

window.mainloop()
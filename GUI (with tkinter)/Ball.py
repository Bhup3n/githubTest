#this is going to be used in the 2d multiple animations

class Ball:

    def __init__(self, canvas, x, y, diameter, x_velocity, y_velocity, colour):      #need to include the initialise
        self.canvas = canvas    #we are saying the self.canvas = the canvas we receive as an argument from the other file
        self.image = canvas.create_oval(x, y, diameter, diameter, fill=colour)   #draws the oval with an x and y coordinate and we repeat diameter twice because it is equal for both the width and height so we fill (width, height) with diameter and we fill the colour with colour that we receive
        self.x_velocity = x_velocity   #setting the x velocity
        self.y_velocity = y_velocity   #setting the y velocity

    def move(self):
        coords = self.canvas.coords(self.image)   #gets coords of the oval
        #this will give us 4 sets of coords, the first 2 are the top coords of the ball and the last 2 are the bottom coords of the ball

        if coords[2] >= self.canvas.winfo_width() or coords[0] < 0:   #if the 3rd set of coords is greater than or equal to the width of the canvas or the 1st set of coords is less than 0
            self.x_velocity = -self.x_velocity       #change to the opposite direction

        if coords[3] >= self.canvas.winfo_height() or coords[1] < 0:     #same thing but with 4th set and 2nd set
            self.y_velocity = -self.y_velocity       #change to opposite direction

        self.canvas.move(self.image, self.x_velocity, self.y_velocity)   #moves the ball at whatever the x velocity and y velocity is at
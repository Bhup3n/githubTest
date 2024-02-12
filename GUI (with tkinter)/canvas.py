from tkinter import *

#canvas = widget used to draw graphs, plots and images in a window

window = Tk()

canvas = Canvas(window,
                height=500,
                width=500)

canvas.create_line(0,0,500,500,               #creates a line from the top right corner(x= 0 and y=0) to the bottom right corner(x=500 and y=500)
                   fill="blue",              #colour of line
                   width=5)              #width of line

# you could do this      Blueline = canvas.create_line(0,0,500,500, fill="blue",width=5)

canvas.create_rectangle(50,100,250,250, fill="red", outline="black")     #creates a red rectangle    outline gives an outline colour

canvas.create_polygon(250,0,400,400,0,400, fill="purple")  #for a polygon, we need x sets of coordinates where x = num of vertices.  in this case we make a triangle so 3 sets are required
#we could do this to speed up the process:
#points = [250,0,400,400,0,400]
#canvas.create_polygon(points, fill="purple")

canvas.create_arc(300,300,500,500,          #these coords actually show how much space it would take instead of it being the starting and end point
                  style=PIESLICE,           #you can change the style of an arc, by default it is a pie slice,   if you want it to just be an arc, we just put ARC
                  start=90,                 #can change what angle the arc is facing, by default it is at 0
                  fill="green",
                  extent=90)               #by default it is 90 but for eg, if we put it at 180, it would become a semi circle

canvas.create_oval(190,190,310,310,fill="yellow")     #creates an oval, coords work like an arc

canvas.pack()

window.mainloop()
#frame = rectangular container to hold and group widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="#6291df",
              bd=5,relief=SUNKEN)      #gives the frame a border with a width of 5 and a sunken relief
frame.pack(side=BOTTOM)    #we put the frame on the bottom of the window

Button(frame,                 #the frame has all the buttons grouped together so they cant seperate if we expand the window
       text="w",
       font=("Consolas", 20),
       width=3).pack(side=TOP)             #this is a shortcut to print and make a button without a name, however this does mean you cant adjust the button by its name anymore
Button(frame, text="a", font=("Consolas", 20), width=3).pack(side=LEFT)      #puts the 3 bottom buttons side by side and w on the top
Button(frame, text="s", font=("Consolas", 20), width=3).pack(side=LEFT)
Button(frame, text="d", font=("Consolas", 20), width=3).pack(side=LEFT)

window.mainloop()
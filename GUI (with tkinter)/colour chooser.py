#this can be used for eg customisation in a game you are making

from tkinter import *
from tkinter import colorchooser

def click():
    colour = colorchooser.askcolor()      #asks user for a colour  (it returns 2 elements, 1 is the amount of red, then green, then blue and then the other is the hex code of the colour)
    print(colour)
    colourhex = colour[1]       #figures out the 2nd element (which is the hex code) and stores it in the variable
    print(colourhex)
    window.config(bg=colourhex)    #change background to the hex value

    #to do it all in 1 line of code:
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()
window.geometry("420x420")

button =Button(text="click me", command=click)
button.pack()


window.mainloop()

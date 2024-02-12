from tkinter import *

# widgets = GUI (with tkinter) elements (buttons, textboxes, labels, images)
# windows = container to contain or hold these widgets

window = Tk()    #creating a new window that can be used
window.geometry("420x420")    #creating the size of the window   (geometry("width x height")
window.title("My first GUI (with tkinter)")    #changes the title of the window from Tk to whatever is in the brackets
window.config(background="black")   #change the background colour of the window


window.mainloop()    #places a window on the computer screen and can listen for events
from tkinter import *

def something(event):         #have to include this event whenever making a parameter including mouse events
    print("d")
    print("your coords are: " + str(event.x)+","+str(event.y))      #event.x and event.y catches wherever your x and y coords are when you click on the GUI (with tkinter) window

window = Tk()

#window.bind("<Button-1>", something)    #if you left click...
#window.bind("<Button-2>", something)#    if you click scroll wheel...
#window.bind("<Button-3>", something)    #if you right click
#window.bind("<ButtonRelease>", something)   #if you hold a button on your mouse, it doesnt do anything but when you let go, the event triggers
#window.bind("<Enter>", something)      #triggers when you entered the GUI (with tkinter) window
#window.bind("<Leave>", something)       #triggers when you leave the GUI (with tkinter) window
window.bind("<Motion>", something)     #triggers when the mouse moves

window.mainloop()
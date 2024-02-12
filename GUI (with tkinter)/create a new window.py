from tkinter import *

def create():
    new_window = Toplevel()  #a new window on top of other windows linked to the bottom window ( window = Tk())   eg if you close the main window, this window would close as well
#   new_window = Tk()        #this would create a new independent window
#   window.destroy()         #destroys the old window after you make a new window

window = Tk()

Button(window, text="create", command=create).pack()

window.mainloop()
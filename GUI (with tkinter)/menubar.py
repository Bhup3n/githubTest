from tkinter import *

def openfile():
    print("you opened a file")

def savefile():
    print("you saved a file")

def cut():
    print("you cut a text")

def copy():
    print("you copy a text")

def paste():
    print("you pasted some text")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)    #set the menu of this window to the menu bar

filemenu = Menu(menubar,                # adds a file menu to our menubar
                tearoff=0,              #tearoff are some lines that appear once we open a file inside of the menu bar so we get rid of it by setting it to 0
                font=("Comic Sans", 15))
menubar.add_cascade(label="file", menu=filemenu)       #adds a drop down file menu
filemenu.add_command(label="open", command=openfile)       #adds an open tab inside the file menu
filemenu.add_command(label="save", command=savefile)       #adds a save tab inside the file menu    ,   the functions are going to be used to have the buttons do something
filemenu.add_separator()                 #adds a separating line between save and exit
filemenu.add_command(label="exit", command=quit)       #adds an exit tab inside the file menu  , quit is a shortcut we can use to not create a seperate function

editmenu = Menu(menubar, tearoff=0, font=("Comic Sans", 15))    #adds an edit to our menu bar
menubar.add_cascade(label="edit", menu=editmenu)
editmenu.add_command(label="cut", command=cut)
editmenu.add_command(label="copy", command=copy)
editmenu.add_command(label="paste", command=paste)


window.mainloop()


#you can add an image by doing this     filemenu.add_command(label="open", command=openfile, image=openimage, compound="left")
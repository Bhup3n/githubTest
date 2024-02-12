from tkinter import *

# button is when you click it then it does stuff

count = 0
def click():
    global count
    count+=1
    print(count)

window = Tk()

photo = PhotoImage(file="photos/pray emoji.png")       #copy image, paste it in the photos directory and then write photos\\the image name

button = Button(window,                          #variable name = Button(variable name)
                text="click me!",                #displays the text     text = "text goes here"
                command=click,                   #does whatever command equals a function (its like calling a function)       commmand = function name WITHOUT THE BRACKETS
                font=("Comic Sans", 30),         #font = font name, font size
                fg="red",                        #fg = foreground colour
                bg="black",                      #bg = background colour
                activeforeground="red",          #this is because without this, when we click the button it would flash colours, so we do this,   activeforeground = "red"
                activebackground="black",        #this is because without this, when we click the button it would flash colours, so we do this,   activebackground = "black"
                #state=DISABLED,                  we do this when we dont want someone clicking the button, this means that the user cant click the button, normally state = ACTIVE
                image=photo,                     #to display photo,  image = variable name
                compound="bottom")               #to move photo relative to text,  compount="preposition"


button.pack()   #displays button



window.mainloop()
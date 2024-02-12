from tkinter import *

#label = area widget that has text or an image within a window

window = Tk()

photo = PhotoImage(file="photos/binary.png")    #copy image, paste it in the photos directory and then write photos\\the image name        this is to have a photo in your label

          # for the line below:              #this has to contain the window's name inside of the brackets so in this case it is just "window"
label = Label(window,                             #we can put line 7,8,9,10,11 together but we seperate them like this to make it easier to read
              text="hello there",                 #text it will display
              font=("Arial", 40, "bold"),         #font = ("fontname", font size, "font style"),
              fg="green",                         #fg = foreground colour
              bg="black",                         #bg = background colour
              relief=RAISED,                      #relief = BORDER STYLE
              bd=10,                              #bd = border width
              padx=20,                            #padx = distance of text from x axis
              pady=20,                            #pady = distance of text from y axis
              image=photo,                        #to make the photo appear     image = variable name
              compound="bottom")                  #place the image relative to the text so its not on top of text     compound = "preposition"


label.pack()   #this adds the label to the window, and if you put any text, by default it would make it go to the top middle of the window
#label.place(x = 100, y = 100)   this does the same thing as pack but you can also choose where to put the text



window.mainloop()
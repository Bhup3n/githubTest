#create a sliding scale

from tkinter import *

def submit():
    print("the temperature is:", scale.get())           #remember, if i put text after the scale.get(), i would have to turn it into a string so...  str(scale.get()), "bla kjhfa"

window = Tk()

fire = PhotoImage(file="photos/fire.png")
label = Label(image=fire)                        #making a label to display the image
label.pack()

scale = Scale(window,
              from_=100, to =0,       #creates our values so 0 is the lowest our scale will go and 100 is the highest   (from needs a _ so it works, without it, it doesnt work
              length=300,
#              oreint=VERTICAL,           can set the orientation of the scale as well
              font=("Arial", 10),          #changes the font and font size of the number next to the slider
              tickinterval=20,            #shows where every 20 degrees are, so it shows 20, 40, 60, 80, 100
              showvalue=True,             #if its true, it shows the exact numbers of your slider, if its false, it doesnt,   can also use 1 and 0 for True and False
              troughcolor="black",        #changes the colour of the thing that is underneath the slider
              fg="red",
              bg="white",
              )

scale.set(50)            #choose what number your scale slider starts on
scale.pack()

button = Button(window,                        #creating a button to submit our temperature
                text="submit",
                command=submit)
button.pack()

window.mainloop()
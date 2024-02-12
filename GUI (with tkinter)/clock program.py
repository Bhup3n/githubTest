from tkinter import *
from time import *

def update():
    time_string = strftime("%H:%M:%S")     #gets the current time
    time_label.config(text=time_string)   #updates the time_labels text with the time_string

    time_label.after(1000, update)  #update time every second, the 1000 means 1000 milliseconds and we are calling a function in its own function

window = Tk()

time_label = Label(window, font=("Arial", 50),fg="green", bg="black")
time_label.pack()

update()


window.mainloop()
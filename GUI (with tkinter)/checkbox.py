from tkinter import *

def display():
    if(x.get() == 1):              #gets info from x and see whether it is ticked or not
        print("you agree")         #if it is ticked, x does = 1
    else:
        print("you disagree")      #if it isnt ticked, x = 0

window = Tk()

photo = PhotoImage(file="photos/agree.png")

x = IntVar()          #x = an integer variable, if it was a string, it would be a string variable (x = StringVar())

check_button = Checkbutton(window,
                           text="i agree",      #text on checkbox
                           variable=x,          #this is used to see whether the user ticked it or not
                           onvalue=1,           #if they ticked it, onvalue = 1         can also set this to True or False, if this is done change x to BooleanVar
                           offvalue=0,          #if they untick, offvalue = 0
                           command=display,
                           font=("Arial", 20),
                           fg="blue",
                           bg="black",
                           activeforeground="blue",
                           activebackground="black",
                           padx=30,
                           pady=10,
                           image=photo,
                           compound="right")
check_button.pack()

window.mainloop()
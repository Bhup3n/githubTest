from tkinter import *

def something(event):         #we have to include the event everysingle time we make a function for a key event, even if we dont use the event
    print("you pressed: " + event.keysym)     #shows what key you pressed due to the even.kysym which means key symbol
    label.config(text=event.keysym)           #disp[ays what key you pressed onto the screen

window = Tk()

window.bind("<Key>", something)     #we use window.bind to bind a function to a key,   window.bind(event, function)
                             #in the  <>  we put the key that we press then the function follows on after that, for eg if we put e in there, the function would execute when we press e
                             #the Key inside of it means almost any key you press

label = Label(window, font=("Arial", 60))      #amkes a label to show the key we pressed
label.pack()

window.mainloop()
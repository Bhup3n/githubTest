from tkinter import *
from tkinter import messagebox         #this imports the message box library

def click():
    messagebox.showinfo(title="info message box", message="this is displayed", icon="error")         #this shows the message box with info   and   you can also change the icon
    #while(True):                                                if you do this, it would keep on repeating the message box even if you close it so it never goes away
    messagebox.showwarning(title="wArNiNg", message="you have a virus")        #this shows a message box but with a warning sign
    messagebox.showerror(title="error", message="something went wrong")        #this shows a message box with an error

    if messagebox.askokcancel(title="as ok cancel", message="do you want to do it"):          #this gives the user 2 options, ok or cancel, if it is ok, then it equals true but if it isnt,
        print("you did it")                                                                      #                                                                      then it is false
    else:
        print("you didnt do it")                      #that line ^ returns a true or false value

    if messagebox.askretrycancel(title="ask retry cancel", message="do you want to retry"):     #this is the same thing as the one above but asks if it wants to retry instead
        print("you retried")
    else:
        print("you didnt retry")            #that line ^ returns a true or false value

    if messagebox.askyesno(title="ask yes or no", message="do you like cake"):      #this asks the user a yes or no question
        print("same")
    else:
        print("me neither")            #that line ^ returns a true or false value

    print(messagebox.askquestion(title="ask question", message="do you like pie"))   #this asks the user a yes or no question
                                      #this line reutrns a string instead ^
    ans = messagebox.askyesnocancel(title="yes,no,cancel", message="do you like to play")        #this asks yes, no or cancel
    if ans == True:
        print("you like to play")
    elif ans == None:
        print("you have avoided the question")  #that line ^ returns a true or false or None value
    else:
        print("you dont like to play")

window = Tk()

button = Button(window,
                command=click,
                text="click me")
button.pack()

window.mainloop()
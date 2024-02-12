from tkinter import *

#entry widget = textbox that acceps a single line of user input

def backspace():
    entry.delete(len(entry.get()) - 1, END)       #get the value of entry, work out the length of it - 1 to get the 2nd to last character's index to delete to delete the last character

def delete():
    entry.delete(0, END)     #deletes everything in entry from index 0 all the way to the last index which we can use END for

def submit():
    username = entry.get()    #gets the current value of entry to know what the user has written
    print("hello", username)
    entry.config(state=DISABLED)     #disables the entry box after the user submits their name

window = Tk()

entry = Entry(window,
              font=("Arial", 20),         #font = font name, font size
              fg="green",                 #foreground colour = green
              bg="black",)                #background colour = black
#             show="*")                   this shows * for every character when you type something instead of the character you put

entry.pack(side=LEFT)        #puts the writing on the left side to have the submit and this side by side

submit_button = Button(window, text="submit", command=submit)        #makes a submit button
submit_button.pack(side=RIGHT)        #put the submit button on the right side

delete_button = Button(window, text="delete", command=delete)       #makes a delete button
delete_button.pack(side=RIGHT)        #puts the delete button on the right side

backspace_button = Button(window, text="backspace", command=backspace)   #makes a backspace button
backspace_button.pack(side=RIGHT)     #puts the backspace button on the right side

window.mainloop()
#this can be used to open the users file

from tkinter import *
from tkinter import filedialog

def open_file():
    filepath = filedialog.askopenfilename()        #this returns a string which is the file path      #you can use initialdir = file path location to open it faster inside of the brackets
    #print(filepath)                               #this will print the location of the file path you choose to open
    file = open(filepath, "r")      #this opens the file and then reads it due to the "r"
    print(file.read())              #prints contents of file
    file.close()                    #closes file

window = Tk()

button = Button(text="open file", command=open_file)
button.pack()

window.mainloop()
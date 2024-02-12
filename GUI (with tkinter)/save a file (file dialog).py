from tkinter import *
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\bhupe\\Desktop",   #changing it so it default goes to the desktop, have to have double back slashes
                                    defaultextension=".txt",             #by default, it saves as a text file
                                    filetypes=[
                                        ("Text file",".txt"),            #can save as a text file
                                        ("HTML file",".html"),           #can save as an HTML file
                                        ("All files", ".*")              #can save as all files
                                    ])

    filetext = str(text.get(1.0, END))        #gets whatever the user has written from begginning to end in a string format
    file.write(filetext)                      #writes to the file
    file.close()

window = Tk()

button = Button(text="save", command=save_file)
button.pack()

text = Text(window)
text.pack()

window.mainloop()
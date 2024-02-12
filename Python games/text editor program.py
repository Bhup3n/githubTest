from tkinter import *
from tkinter import colorchooser, font
from tkinter.messagebox import *

def change_colour():
    colour = colorchooser.askcolor(title="pick a colour")      #lets user pick a colour
    text_area.config(fg=colour[1])       #the hex value of the colour you choose lets you change the colour of your text

def change_font(*args):     #*args is for when a function receives a varying amount of arguments
    text_area.config(font=(font_name.get(), size_box.get()))   #lets user choose font and the font size

def cut():
    text_area.event_generate("<<Cut>>")       #lets you cut

def copy():
    text_area.event_generate("<<Copy>>")      #lets you copy

def paste():
    text_area.event_generate("<<Paste>>")     #lets you paste

def about():
    showinfo("About this program", "This is a program written by me")     #the title of the new window it shows and then the message on the window

def quit():
    window.destroy()        #closes the window


window = Tk()
window.title("Notepad")
file = None

window_width = 500
window_height= 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width /2))
y = int((screen_height / 2) - (window_height /2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))        #these past 6 lines of code get the window to start off in the middle

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))       #makes a text area with a font of Arial and a size of 25

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)                                          #as a result of these 3 lines of code,  the text will make a new line once it reaches a border
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)      #north + east = south + west
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)         #creates a scroll bar to the right and we add the scroll bar to the text area

frame = Frame(window)
frame.grid()

colour_button = Button(frame, text="colour", command=change_colour)
colour_button.grid(row=0, column=0)


font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)  #makes an option menu and the *font families lets you choose from all the fonts
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)   #lets you change size of font from 1 to 100
size_box.grid(row=0, column=2)


menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)           #creates a file menu for only exit
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)           #creates an edit menu for cut, copy and paste
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)          #creates a help menu for only about
help_menu.add_command(label="About", command=about)


window.mainloop()
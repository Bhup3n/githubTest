#create a weather app

def title_labels(tab, city):
    Label(tab, text=city + " Weather Info", font=("Arial", 50, "underline")).pack()  # creates a title label
    Label(tab, text="Day", font=("Arial", 30, "underline")).place(x=340, y=200)  # creates a day label at the top
    Label(tab, text="Temperature", font=("Arial", 30, "underline")).place(x=770, y=200)  # creates a temperature label at the top
    Label(tab, text="Chance of Rain", font=("Arial", 30, "underline")).place(x=1300, y=200)     #creates a chance of rain label at the top


def info(tab, day, horizontal1, vertical1, temp, horizontal2, vertical2, rain, horizontal3, vertical3):
    Label(tab, text=day, font=("Comic Sans", 25)).place(x=horizontal1, y=vertical1)          #adds in info for day number
    Label(tab, text=temp, font=("Comic Sans", 25)).place(x=horizontal2, y=vertical2)         #adds in label for temperature of that day
    Label(tab,text=rain, font=("Comic Sans", 25)).place(x=horizontal3, y=vertical3)          #adds in label for rain chance of that day

from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1920x1080")

notebook = ttk.Notebook(window)
tab1 = Frame(notebook)       #creates a frame for tab1
tab2 = Frame(notebook)          #creates a frame for tab1
notebook.add(tab1, text="Crawley")
notebook.add(tab2, text="London")
notebook.pack(expand=True, fill="both")

#crawley weather
title_labels(tab1, "Crawley")

info(tab1, "friday", 340, 300, "13°C", 840, 300, "13%", 1400, 300)
info(tab1, "Saturday", 340, 500, "8°C", 840, 500, "89%", 1400, 500)
info(tab1, "Sunday", 340, 700, "3°C", 840, 700, "100%", 1400, 700)

#London weather
title_labels(tab2, "London")

info(tab2, "friday", 340, 300, "28°C", 840, 300, "3%", 1400, 300)
info(tab2, "Saturday", 340, 500, "31°C", 840, 500, "1%", 1400, 500)
info(tab2, "Sunday", 340, 700, "24°C", 840, 700, "2%", 1400, 700)

window.mainloop()
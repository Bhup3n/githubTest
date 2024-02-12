from tkinter import *
from tkinter import ttk

#creates multiple tabs in one window

window = Tk()
window.geometry("1920x1080")

notebook = ttk.Notebook(window)  #widget that manages a collection of windows and displays

tab1 = Frame(notebook)   #new frame for tab1
tab2 = Frame(notebook)   #new fram for tab2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="tab 2")
notebook.pack(expand=True,      #expand to fill any space not otherwise used
              fill="both")      #fill space on x and y axis

Label(tab1, text="this is in tab1", width=40, height=20, padx=20, pady=20, font=("Arial", 50)).pack(side=BOTTOM)
Label(tab2, text="this is in tab2", width=40, height=20, padx=20, pady=20, font=("Arial", 50)).pack(side=BOTTOM)

window.mainloop()
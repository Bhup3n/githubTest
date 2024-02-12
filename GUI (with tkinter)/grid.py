from tkinter import *

#grid() = organise widgets in a container  (in a table like structure)

window = Tk()

title = Label(window, text="enter info", font=("Arial", 13)).grid(row=0, column=0, columnspan=2)        #title label

first_name_label = Label(window, text="first name: ").grid(row=1,column=0)   #instead of pack, we use grid to put the label on row = index 0 and column = index 0
first_name_entry = Entry(window).grid(row=1, column=1)

surname = Label(window, text="last name: ").grid(row=2, column=0)
surname_entry = Entry(window).grid(row=2, column=1)

email = Label(window, text="email: ").grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submit = Button(window, text="submit").grid(row=4, column=0,columnspan=2)   #columns span means it takes up 2 columns so it takes up column 0 and 1

window.mainloop()
from tkinter import *

#in this you can enter multiple lines of text
def submit():
    input = text.get("1.0", END)     #we want to get what the user has written so we get it from the first line to the end line (index)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20, "bold"),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="blue")
text.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()
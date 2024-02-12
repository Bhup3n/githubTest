from tkinter import *

def button_press(num):
    global equation_text

    equation_text = equation_text + str(num)           #for any character we type, we convert it into a string
    equation_label.set(equation_text)         #then we set the text to the label. and all together we have whatever the user types displayed to the label

def equals():
    global equation_text

    try:
        total = str(eval(equation_text))         #calculates result of equation and converts answer to a string
        equation_label.set(total)             #sets the result as the label

        equation_text = total     #lets us reuse the result

    except ZeroDivisionError:

        equation_label.set("arithmetic error")                #this is just so if the computer cant solve a problem divided by 0, it will print this instead of the error
        equation_text = ""

    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""

def clear():
    global equation_text

    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("calculator")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=("Consolas", 20), bg="white", width=24, height=2)   #makes the label at the top to display the characters we enter
label.pack()

frame = Frame(window)
frame.pack()

#we are about to add the buttons
button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))    #calling for button press function
button1.grid(row=0, column=0)
#
button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))    #calling for button press function
button2.grid(row=0, column=1)
#
button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))    #calling for button press function
button3.grid(row=0, column=2)
#
button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))    #calling for button press function
button4.grid(row=1, column=0)
#
button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))    #calling for button press function
button5.grid(row=1, column=1)
#
button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))   #calling for button press function
button6.grid(row=1, column=2)
#
button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))    #calling for button press function
button7.grid(row=2, column=0)
#
button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))    #calling for button press function
button8.grid(row=2, column=1)
#
button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))    #calling for button press function
button9.grid(row=2, column=2)
#
button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))    #calling for button press functionn
button0.grid(row=3, column=0)
#
plus = Button(frame, text="+", height=4, width=9, font=35,
                 command=lambda: button_press("+"))    #calling for button press function
plus.grid(row=0, column=3)
#
minus = Button(frame, text="-", height=4, width=9, font=35,
                 command=lambda: button_press("-"))    #calling for button press function
minus.grid(row=1, column=3)
#
multiply = Button(frame, text="*", height=4, width=9, font=35,
                 command=lambda: button_press("*"))    #calling for button press function
multiply.grid(row=2, column=3)
#
divide = Button(frame, text="/", height=4, width=9, font=35,
                 command=lambda: button_press("/"))    #calling for button press function
divide.grid(row=3, column=3)
#
equal = Button(frame, text="=", height=4, width=9, font=35,
                 command=equals)   #calling for equal function
equal.grid(row=3, column=2)
#
decimal = Button(frame, text=".", height=4, width=9, font=35,
                 command=lambda: button_press("."))    #calling for button press function
decimal.grid(row=3, column=1)
#
clear = Button(window, text="clear", height=4, width=39, font=35,
                 command=clear)    #calling for clear function
clear.pack()


window.mainloop()
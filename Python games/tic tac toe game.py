from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:   #if the button clicked is empty and there isnt a winner yet:

        if player == players[0]:                       #if it is player 1 turn (the x)
            buttons[row][column]["text"] = player      #the button clicked that is empty is now x

            if check_winner() is False:                #if there is no winner still
                player = players [1]                   # it is now player 2 turn (the o)
                label.config(text=(players[1] + " turn"))          #print o turn

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie"))

        else:                                            #this is now if it is player 2 turn

            buttons[row][column]["text"] = player      #the button clicked that is empty is now o

            if check_winner() is False:                #if there is no winner still
                player = players [0]                   # it is now player 1 turn (the X)
                label.config(text=(players[0] + " turn"))          #print X turn

            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie"))


def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":#if there are 3 in a row and it doesnt = to an empty space, then return true
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")          #the buttons that win turn green
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":   #if there are 3 in a column return true
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":  #if there are 3 diagonal from top left to bottom right
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":  #if there are 3 diagonal from top right to bottom left
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:      #if there are no empty spaces and no winner has been declared then...

        for row in range(3):

            for column in range(3):
                buttons[row][column].config(bg="yellow")      #if its a tie all buttons turn yellow
        return "Tie"

    else:                    #if there are empty spaces and no winner has been declared... then
        return False

def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":     #if there are any spaces left when we click one
                spaces -= 1      #then - 1 space

    if spaces == 0:     #if there are no spaces left
        return False
    else:                #if there are spaces left
        return True

def new_game():

    global player

    player = random.choice(players)   #chooses a random player to start the game again

    label.config(text=player + " turn")     #shows whos turn it is

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")         #reset the buttons to be completely blank


window = Tk()
window.title("tic tac toe")
players = ["x", "o"]    #its cross versus circle
player = random.choice(players)   #choose who starts first at random from the players list
buttons = [ [0,0,0],       #first row
          [0,0,0],         #second row
          [0,0,0] ]        #third row

label = Label(text=player + " turn", font=("Arial", 40))
label.pack(side="top")

reset_button = Button(text="reset", font=("Arial", 20), command=new_game)   #creating a reset button
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("Arial", 40), width=5, height=2,        #creates 9 buttons in a 3 by 3 grid
                                      command = lambda row=row, column = column: next_turn(row, column))   #create a function
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
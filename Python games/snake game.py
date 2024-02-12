from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 1000
SPEED = 75            #the lower the number the faster the game
SPACE_SIZE = 50
BODY_PARTS = 3       #how many body parts the snake has when we begin a game
SNAKE_COLOUR = "green"
FOOD_COLOUR = "red"
BACKGROUND_COLOUR = "black"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coords = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coords.append([0, 0])      #snake starts at top left

        for x, y in self.coords:
            square = canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
            self.squares.append(square)

class Food:

    def __init__(self):    #constructs our food
        x = random.randint(0, GAME_WIDTH/SPACE_SIZE -1 ) * SPACE_SIZE   #this chooses random place to put food on x axis, 700/50-1 = 13. whatever the random num is * 50
        y = random.randint(0, GAME_HEIGHT/SPACE_SIZE - 1) * SPACE_SIZE     #this chooses random place to put food on y axis, 700/50-1 = 13. whatever the random num is * 50

        self.coords = [x, y]    #gets the coords

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR,         #makes an oval for a food, the coords show how much space the oval would take
                           tag="food")    #the tag is so we can refer to this as food

def next_turn(snake, food):
    x,y = snake.coords[0]   #head of snake

    if direction == "up":
        y -= SPACE_SIZE      #moves one space up

    elif direction == "down":
        y += SPACE_SIZE      #moves one space down

    elif direction == "left":
        x -= SPACE_SIZE      #moves one space left

    elif direction == "right":
        x += SPACE_SIZE      #moves one space right

    snake.coords.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)    #add a square

    snake.squares.insert(0, square)

    if x == food.coords[0] and y == food.coords[1]:   #this is for when we hit a food

        global score

        score += 1
        label.config(text="Score: " + str(score))    #add one to score and print it off
        canvas.delete("food")     #delete that food
        food = Food()   #make a new food

    else:

        del snake.coords[-1]    #deletes snakes last body part

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):   #if snake collides, then call gamme over

        game_over()

    else:    #if it doesnt, then next turn

        window.after(SPEED, next_turn, snake, food)    #calls next turn function again and we pass in our arguments of snake and food

def change_direction(new_direction):

    global direction

    if new_direction == "left":       #if the player turns left
        if direction != "right":      #and the way the player was heading before wasnt right (so we dont do a 180 turn)
            direction = new_direction     #then direction = the new direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction

    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coords[0]

    if x < 0 or x >= GAME_WIDTH:    #if x coordinate head goes off screen, then
        return True
    elif y < 0 or y >= GAME_HEIGHT:   #if y coordinate head goes off screen then
        return True

    for body_part in snake.coords[1:]: #for every body part after the head of the snake
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)    #deletes everytghing in canvas
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font =("Arial", 70), text="game over",fill="red", tag="gameover")    #creates a new text box called game over


window = Tk()
window.title("snake game")
window.resizable(False, False)       #if you dont want the window to be resizable then pass in false twice

score = 0
direction = "down"

label = Label(window, text="Score: " + str(score), font=("Arial", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)     #gives a black canvas to the window underneath the score label
canvas.pack()

window.bind("<Left>", lambda event: change_direction("left"))      #moves the snake left when you touch the left arrow key
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Down>", lambda event: change_direction("down"))
window.bind("<Up>", lambda event: change_direction("up"))

snake = Snake()   #calling snake class
food = Food()   #calling food class

next_turn(snake, food)

window.mainloop()
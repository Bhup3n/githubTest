import pygame
pygame.init()           #should use this all the time to initialise pygame

#constant variables
WIDTH = 1820        #window width
HEIGHT = 980         #window height
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 70
RECTANGLE_VELOCITY = 5
BALL_X_VELOCITY = 6
BALL_Y_VELOCITY = 5
RED_HIT = pygame.USEREVENT + 1     #amkes these as events
BLUE_HIT = pygame.USEREVENT + 2    #the numbers dont matter, it can be 2413 if you wanted it to but there has to be some number to differentiate the events

#variables that will change
ball_off = False        #the ball is off the screen
red_score = 0
blue_score = 0
rally = 0


window = pygame.display.set_mode((WIDTH, HEIGHT))    #create the window
pygame.display.set_caption("PING PONG")     #changes name of window to ping pong

red = pygame.Rect(50, HEIGHT//2, 10, 200)     #create the rectangle on the left (x coord, y coord, width, height
blue = pygame.Rect(WIDTH - 50, HEIGHT//2, 10, 200)    #create blue rectangle
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 20, 20)     #create a rectangle to represent hitbox of a ball

border = pygame.Rect(WIDTH//2 - 6, 0, 1, HEIGHT)     #makes a border in the middle


def red_move(keys_pressed):
    if keys_pressed[pygame.K_w] and red.y - RECTANGLE_VELOCITY > 0:    #if w is pressed, red moves up at whatever rectangle velocity is set to. the and is so it cant go above the screen
        red.y -= RECTANGLE_VELOCITY
    if keys_pressed[pygame.K_s] and red.y + RECTANGLE_VELOCITY + red.height < HEIGHT:       #if s is pressed, red moves down. the and is so it cant go below the screen
        red.y += RECTANGLE_VELOCITY

def blue_move(keys_pressed):
    if keys_pressed[pygame.K_UP] and blue.y - RECTANGLE_VELOCITY > 0:     #up means the arrow key
        blue.y -= RECTANGLE_VELOCITY
    if keys_pressed[pygame.K_DOWN] and blue.y + RECTANGLE_VELOCITY + blue.height < HEIGHT:     #down means the arrow key
        blue.y += RECTANGLE_VELOCITY


def ball_move(ball):
    global BALL_X_VELOCITY, BALL_Y_VELOCITY, ball_off  # we global these and not put them as arguments because we want the whole program to get the value of them and not just the functions

    if ball.y > HEIGHT - 15 or ball.y < 0:    #if ball hits top or bottom, it bounces
        BALL_Y_VELOCITY *= -1

    if ball.x > WIDTH - 15 or ball.x < 0:
        ball_off = True       #sets ball off to True and stops drawing the ball if it is off the screen

    if red.colliderect(ball):    #if the ball hits red rectangle
        BALL_X_VELOCITY *= -1
        pygame.event.post(pygame.event.Event(RED_HIT))    #we post these events so that we can say that event.type == RED_HIT

    if blue.colliderect(ball):    #if ball hits blue rectangle
        BALL_X_VELOCITY *= -1
        pygame.event.post(pygame.event.Event(BLUE_HIT))

    ball.x += BALL_X_VELOCITY
    ball.y += BALL_Y_VELOCITY

def winner(text):
    draw_text = pygame.font.SysFont("comicsans", 100).render(text, 1, WHITE)    #creates a text for the winner
    window.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT//2 - draw_text.get_height()//2))    #displays the text in the middle
    pygame.display.update()    #update the display with the text
    pygame.time.delay(5000)   #delay time for 5 seconds


def draw_window(rally):               #draws our window
    window.fill(BLACK)

    pygame.draw.rect(window, WHITE, border)

    rally_text = pygame.font.SysFont("comicsans", 40).render("rally score: " + str(rally), 1, WHITE)   #creates red score text, the 1 is alsways necessary
    window.blit(rally_text, (WIDTH//2 - rally_text.get_width()//2, 10))

    pygame.draw.rect(window, RED, red)    #draws red rectangle
    pygame.draw.rect(window, BLUE, blue)   #draws blue rectangle

    if ball_off == False:     #only draws the ball if it is on the screen
        pygame.draw.circle(window, WHITE, (ball.x, ball.y), 10)

    pygame.display.update()


def main():
    global red_score, blue_score, rally, BALL_X_VELOCITY, BALL_Y_VELOCITY     #have to global these

    clock = pygame.time.Clock()    #creates a clock
    run = True
    while run:
        clock.tick(FPS)    #refreshes window every FPS number times per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == RED_HIT:
                rally += 1              #rally is increases by 1
                red_score += 1    #red score is increased by 1
                BALL_X_VELOCITY += 2    #the balls horizontal velocity is increased by 1
            if event.type == BLUE_HIT:
                rally += 1
                blue_score += 1
                BALL_Y_VELOCITY += 3    #the ball y velocity is increased by 1

        winner_text = ""
        if ball_off == True:
            if red_score == blue_score:      #this means red last touched the ball
                winner_text = "Red Wins!"
            if blue_score > red_score:       #this means blue last touched the ball
                winner_text = "Blue Wins!"

        if winner_text != "":    #if there is a winner
            winner(winner_text)    #call the winner function
            break    #close the program after the winner function

        keys_pressed = pygame.key.get_pressed()    #figures out whethter a  key is being pressed or not
        red_move(keys_pressed)   #calls the moving function
        blue_move(keys_pressed)
        ball_move(ball)

        draw_window(rally)



    pygame.quit()

if __name__ == "__main__":
    main()
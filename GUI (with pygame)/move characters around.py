import pygame
import os

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VELOCITY = 5    #the speed

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

yellow_spaceship_image = pygame.image.load(os.path.join("photos", "yellow_spaceship.png"))
red_spaceship_image = pygame.image.load(os.path.join("photos", "red_spaceship.png"))

yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
red_spaceship = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)
red_spaceship = pygame.transform.rotate(red_spaceship, 270)

def yellow_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # this is if the a key is pressed (the left key)     the k has to be capatilaised K
        yellow.x -= VELOCITY  # moves 5 pixels to the left
    if keys_pressed[pygame.K_d]:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w]:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s]:
        yellow.y += VELOCITY

def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:     #use arrow keys
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT]:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP]:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN]:
        red.y += VELOCITY


def draw_window(red, yellow):
    window.fill(WHITE)

    window.blit(yellow_spaceship, (yellow.x, yellow.y))     #figures out the position of the yellow spaceship
    window.blit(red_spaceship, (red.x, red.y))    #figures out the position of the red spaceship

    pygame.display.update()



def main():    #main game loop
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)    #makes a rectangle called red that has the same size as the spaceships
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)    #(x coordinate, y coordinate, width, height)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()   #every single time this while loop runs (70 times a second), it will tell us what keys are being pressed
        yellow_move(keys_pressed, yellow)     #calls the yellow move function
        red_move(keys_pressed, red)       #calls the red move function

        draw_window(red, yellow)


    pygame.quit()

if __name__ == "__main__":
    main()
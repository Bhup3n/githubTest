import pygame
import os

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

border = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)     #creates a rectangle in the middle of the screen with a width of 10 and the height of the window

yellow_spaceship_image = pygame.image.load(os.path.join("photos", "yellow_spaceship.png"))
red_spaceship_image = pygame.image.load(os.path.join("photos", "red_spaceship.png"))

yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
red_spaceship = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)
red_spaceship = pygame.transform.rotate(red_spaceship, 270)

def yellow_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:    #if when subtracting the velocity from the spaceship position, then allow to press the key otherwise dont
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < border.x:     #make sure no part of the image goes over the border
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15:    #we use the - 15 because the image was dropping a bit below the screen
        yellow.y += VELOCITY

def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > border.x + border.width:    #cant move left of the border
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:     #cant mover off screen
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 15:
        red.y += VELOCITY


def draw_window(red, yellow):
    window.fill(WHITE)
    pygame.draw.rect(window, BLACK, border)    #draws the border, args = where you want to draw it, the colour, what you are drawing

    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))

    pygame.display.update()



def main():    #main game loop
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)

        draw_window(red, yellow)


    pygame.quit()

if __name__ == "__main__":
    main()
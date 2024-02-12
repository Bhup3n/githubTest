import pygame
import os

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)       #creates a red bullet
YELLOW = (255, 255, 0)    #creates a yellow bullet
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VELOCITY = 5
BULLET_VELOCITY = 7   #how fast the projectiles will be
MAX_BULLETS = 4

YELLOW_HIT = pygame.USEREVENT + 1     #create an event (the numbers have to be different otherwise if they were the same, they would be the sam event)
RED_HIT = pygame.USEREVENT + 2    #the numbers do not matter

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

border = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

space_image = pygame.image.load(os.path.join("photos", "space.png"))
space = pygame.transform.scale(space_image, (WIDTH, HEIGHT))                     #creates a space background

yellow_spaceship_image = pygame.image.load(os.path.join("photos", "yellow_spaceship.png"))
red_spaceship_image = pygame.image.load(os.path.join("photos", "red_spaceship.png"))

yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
red_spaceship = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)
red_spaceship = pygame.transform.rotate(red_spaceship, 270)

def yellow_move(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY > 0:
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY + yellow.width < border.x:
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY > 0:
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY + yellow.height < HEIGHT - 15:
        yellow.y += VELOCITY

def red_move(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY > border.x + border.width:
        red.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY + red.width < WIDTH:
        red.x += VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - VELOCITY > 0:
        red.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY + red.height < HEIGHT - 15:
        red.y += VELOCITY


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VELOCITY      #moves the bullet to the right
        if red.colliderect(bullet):    #if yellow has collided with the bullet
            pygame.event.post(pygame.event.Event(RED_HIT))   #saying the red was hit
            yellow_bullets.remove(bullet)    #removes the bullet
        elif bullet.x > WIDTH:                #if the bullet hits the edge, it destroys the bullet
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY   #moves the bullets to the left
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))      #when we post these events, they get added to the for event in pygame.event.get():
            red_bullets.remove(bullet)
        elif bullet.x < 0:            #if bullet hits edge, it destroys bullet
            red_bullets.remove(bullet)


def draw_window(red, yellow, red_bullets, yellow_bullets):
    window.blit(space, (0,0))     #shows the space background
    pygame.draw.rect(window, BLACK, border)

    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(window, RED, bullet)    #draws a red bullet

    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW, bullet)

    pygame.display.update()



def main():    #main game loop
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []     #making a list of bullets
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:      #if left control button is pressed and the amount of bullets on the screen is less than our max
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)  #bullet that comes from the middle of the ship at a width and height of 10 and 5
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:      #if right control button is pressed
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)  # bullet that comes from the middle of the ship at a width and height of 10 and 5
                    red_bullets.append(bullet)

            if event.type == RED_HIT:     #we know if they got hit or not because we posted the event to the for loop we have above us
                red_health -= 1    #minus one health

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins"

        if yellow_health <= 0:
            winner_text = "Red Wins"

        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets)


    pygame.quit()


if __name__ == "__main__":
    main()
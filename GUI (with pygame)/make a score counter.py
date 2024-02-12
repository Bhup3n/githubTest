import pygame
import os
pygame.font.init()   #initialises the pygame font library

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
FPS = 70
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
VELOCITY = 5
BULLET_VELOCITY = 7
MAX_BULLETS = 4
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)   #creating a font for the health
WINNER_FONT = pygame.font.SysFont("comicsans", 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

border = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

space_image = pygame.image.load(os.path.join("photos", "space.png"))
space = pygame.transform.scale(space_image, (WIDTH, HEIGHT))

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
        bullet.x += BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VELOCITY
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    window.blit(space, (0,0))
    pygame.draw.rect(window, BLACK, border)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)  #creates text, the 1 is always necessary and the white is the colour
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    window.blit(red_health_text, (700, 30))   #displays red health on right side of screen
    window.blit(yellow_health_text, (5, 30))  #displays yellow health on left side of screen

    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))


    for bullet in red_bullets:
        pygame.draw.rect(window, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(window, YELLOW, bullet)

    pygame.display.update()


def winner(text):         #this function will pause the game when someone wins and then restart after
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    window.blit(draw_text, (WIDTH//2 - draw_text.get_width()//2, HEIGHT/2 - draw_text.get_height()//2))    #displays text in middle
    pygame.display.update()
    pygame.time.delay(5000)   #delays for 5000 milliseconds (5 secs)



def main():    #main game loop
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
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
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)

            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins"

        if yellow_health <= 0:
            winner_text = "Red Wins"

        if winner_text != "":
            winner(winner_text)   #calls winner function and restarts the game after 5 seconds
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)


    pygame.quit()


if __name__ == "__main__":
    main()
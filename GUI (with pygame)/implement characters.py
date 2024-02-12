import pygame
import os       #we are going to use this for the photos

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 60
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40    #this is so we can use them later on as well if needed

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")

yellow_spaceship_image = pygame.image.load(os.path.join("photos", "yellow_spaceship.png"))      #imports the yellow spaceship image we have
red_spaceship_image = pygame.image.load(os.path.join("photos", "red_spaceship.png"))    #imports the red spaceship image we have

yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))   #resizes our spaceship to width in width and height in height
red_spaceship = pygame.transform.scale(red_spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

yellow_spaceship = pygame.transform.rotate(yellow_spaceship, 90)    #rotates the yellow spaceship 90 degrees to the right
red_spaceship = pygame.transform.rotate(red_spaceship, 270)        #rotates the red spaceship 270 degrees to the right


def draw_window():
    window.fill(WHITE)

    window.blit(yellow_spaceship, (300, 100))  #use blit to draw the spaceship on, the 2 numbers are where we want to place the image on x and y coordinate
    window.blit(red_spaceship, (700, 100))

    pygame.display.update()



def main():    #main game loop

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()


    pygame.quit()

if __name__ == "__main__":
    main()
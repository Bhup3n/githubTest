import pygame

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)
FPS = 60    #how many times it will refresh per second

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")


def draw_window():
    window.fill(WHITE)
    pygame.display.update()

def main():    #main game loop

    clock = pygame.time.Clock()   #creates a clock
    run = True
    while run:
        clock.tick(FPS)    #runs this program at 60 frames a second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()


    pygame.quit()

if __name__ == "__main__":
    main()
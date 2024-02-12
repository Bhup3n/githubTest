import pygame

WIDTH = 900
HEIGHT = 500
WHITE = (255, 255, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")    #changes the window name

def draw_window():
    window.fill(WHITE)  # fills the colour with RGB values, so 255 red, 255 green, 255 blue which turns out to be white.  have to use double brackets (but in this we dont have to because white already has a pair of brackets
    pygame.display.update()  # use this to update the screen

def main():    #main game loop

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()        #calls the draw window function so we can display it on the window


    pygame.quit()

if __name__ == "__main__":
    main()
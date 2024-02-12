import pygame

WIDTH = 900
HEIGHT = 500

window = pygame.display.set_mode((WIDTH, HEIGHT))    #creates the window and you need the double brackets

def main():

    run = True
    while run:
        for event in pygame.event.get():        #this is code so that the window closes when we want it to close
            if event.type == pygame.QUIT:
                run = False

        # if we want to add something to the window, we have to add it in here

    pygame.quit()

if __name__ == "__main__":
    main()        #making sure it only runs the main function if we run the python file directly
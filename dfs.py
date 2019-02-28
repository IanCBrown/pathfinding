import pygame
import numpy as np
from grid import Grid
from grid import Position
from grid import make_grid

def traversal(Grid):
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = (510, 510)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pathfinding")


     # Loop until the user clicks the close button.
    done = False
    
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        
        # start working
        visited = []

        screen.fill(Grid.BLACK)

        pygame.display.flip()
    
        # Limit to 60 frames per second
        clock.tick(60)
    
    # Close the window and quit.
    pygame.quit()



#create new Grid object for testing 
input_grid = np.zeros(shape=(20,20))
Grid = make_grid(input_grid)
Grid.print_grid()

traversal(Grid)
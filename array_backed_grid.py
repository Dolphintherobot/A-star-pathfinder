

def get_coordinates():
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]
        return (x,y)

def map_to_grid(grid,width,margin,x,y):
    x = x//(width+margin)
    y =y//(width+margin)
    grid[x][y] = 1        






import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (255, 255)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 

grid  = [[0 for x in range(10)] for y in range(10)]
grid[1][5] =1

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_y,mouse_x = get_coordinates()
            map_to_grid(grid,width,margin,mouse_x,mouse_y)


    

 



    
 
    # --- Game logic should go here
    
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    
    height = 20
    width = 20
    margin = 5
    squares = 10
    x = 5
    y = 5
    for row in range(0,margin*squares,margin):
        for column in range(0,margin*squares,margin):
            square = pygame.Rect((x,y),(width,height))
            grid_x = x//25
            grid_y =y//25
            if grid[grid_y][grid_x] == 1:
                color = GREEN
            else:
                color = RED
            pygame.draw.rect(screen,color,square)
            x += width + margin
        x = 5
        y += height + margin
    

        #grabs the position of the players mouse
        
    
   
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


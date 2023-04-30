
import pygame



def get_coordinates():
    '''Purpose:to get the position of the players mouse
    :return y: the position of the click on the gui on the y axis
    :return x: the coordinate of the click on the gui on the x axis '''
    player_position = pygame.mouse.get_pos()
    x = player_position[1]
    y = player_position[0]
    return (x,y)

def map_to_grid(grid,width,margin,x,y):
    '''Purpose:maps a point on the gui and transfers it to the array backed grid
    Post-condtions:will modify the coordinate on the grid to become a 2'''
    x = x//(width+margin)
    y =y//(width+margin)
    grid[x][y] = 2

def draw_squares(screen,grid,height,width,margin):
    ''''Purpose: to draw the squares into the gui
    :parm screen: the display being drawn onto
    :param grid: a nested list,representing the array backed grid
    :param height:how tall you want the squares to be
    :param width: width of the squares
    :param margin: how much space between the squares
    '''

    n = len(grid) 
    m = len(grid[0]) 

    
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    for row in range(n):
        for column in range(m):
            color = WHITE
            if grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 1:
                color = GREEN
            


            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])       

 
#some colors defined in RGB
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
#size of squares and screen
height = 20
width = 20    
margin = 5
size = (255, 255)
screen = pygame.display.set_mode(size)


n = 10 #how many rows 
m = 10 #how many columns
 
pygame.display.set_caption("My Game")
grid  = [[0 for x in range(n)] for y in range(m)]

done = False
 
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = get_coordinates()
            map_to_grid(grid,width,margin,mouse_x,mouse_y)

    

    screen.fill(BLACK)
    draw_squares(screen,grid,height,width,margin)

    
    
    
    pygame.display.flip()
 
    clock.tick(60)
 

pygame.quit()


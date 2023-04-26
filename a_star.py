

import open_vertices as ov
import numpy as np

def distance_calculator(current,goal):
    """Purpose: calculates the manhattin distance between 2 points
    :param current: a tuple of x,y coordinates representing the current path
    :param goal: a tuple of x,y coordinates representing the end of path
    :return F: the number representing the mahattin distance"""

    x,y = current
    end_x,end_y = goal
    F = (end_x+end_y) - (x+y)
    return abs(F)



def square_generator(current,grid,taken):
    '''
    Purpose: will generate a list of coordinates surrounding the current position in a   
    in a square pattern
    param current: a x,y tuple representing the current position
    param grid: a 2d list you are trying to find a path towards
    param taken: a list of previously taken coordinates
    return valid_coordinates: a list of x,y tuples representing valid choices for the next shortest path

    '''

    valid_coordinates = []
    n = len(grid) -1
    m  = len(grid[0]) -1
    top_left_x = current[0] -1
    top_left_y = current[1] - 1

    for x in range(top_left_x,top_left_x+3):
        for y in range(top_left_y,top_left_y+3):
            if x < 0 or x > n:
                continue
            elif y < 0 or y > m:
                continue
            elif (x,y) in taken:
                continue
            else:
                coordinate = (x,y)
                valid_coordinates.append(coordinate)
    return valid_coordinates



def insert_grid(grid,closed_vertices,start):
    '''
    Purpose: will insert the calculated shortest path into the grid
    :parm grid: a 2d list,
    :param closed_vertices: a list of tuples containing current_location and previous_location
    respective order
    :param start: a x,y tuple containing the starting position
    returns None
    Post-conditions: will modify the grid to contain 1's in the specified locations
    '''

    current,previous = closed_vertices[-1]
    x,y = start
    grid[x][y] = 1

    while current != start:
        x,y = current
        grid[x][y] = 1
        
        for tuple in closed_vertices:
            if tuple[0] == previous:
                current,previous = tuple
    
    




def find_path(grid,start,end,print_grid= False):
    '''Purpose: will grab new open vertices and add them to open_vertices list
    
    param grid: an nxm grid 
    param start: the starting position represented with an x,y tuple
    param end: the ending postion represented with x,y tuple
    '''
    taken_spaces = []
    closed_vertices = []
    open_vertices = ov.open_vertices()

    open_vertices.insert(0,start,None)
    current = None
    previous = None


    while current != end and not open_vertices.is_empty():
        previous = current
        current = open_vertices.get_current()
        taken_spaces.append(current)
        closed_vertices.append((current,previous))


        valid_coordinates = square_generator(current,grid,taken_spaces)

        for coordinate in valid_coordinates:
            F = distance_calculator(coordinate,end)
            if not open_vertices.coordinate_is_in(F,coordinate,current):
                open_vertices.insert(F,coordinate,current)
    

    if current == end:
        insert_grid(grid,closed_vertices,start)
        if print_grid:
            print(np.array(grid))
        return True
    else:
        return False

     


grid = [[0 for n in range(10)] for m in range(10)]

start = (0,0)
end = (9,9)
find_path(grid,start,end,True)



        
            
            

                

    

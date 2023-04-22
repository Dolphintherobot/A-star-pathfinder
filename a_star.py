



def distance_calculator(current,goal):
    """Purpose: calculates the manhattin distance between 2 points
    :param current: a tuple of x,y coordinates representing the current path
    :param goal: a tuple of x,y coordinates representing the end of path
    :return F: the number representing the mahattin distance"""

    x,y = current
    end_x,end_y = goal
    F = (end_x+end_y) - (x+y)
    return abs(F)





def find_path(grid,start,end):
    '''Purpose: will grab new open vertices and add them to open_vertices list
    
    param grid: an nxm grid 
    param start: the starting position represented with an x,y tuple
    param end: the ending postion represented with x,y tuple
    '''



    n = len(grid) -1
    m  = len(grid[0]) -1
    current = start
    previous = None


    while current != end:



        
        top_left_x = current[0] -1
        top_left_y = current[1] - 1

        for x in range(top_left_x,top_left_x+3):
            for y in range(top_left_y,top_left_y+3):
                if x < 0 or x > n:
                    continue
                elif y < 0 or y > m:
                    continue
                elif (x,y) in closed_vertices:
                    continue
            
            

                

    

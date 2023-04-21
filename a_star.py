import Llist as L






def distance_calculator(current,goal):
    """Purpose: calculates the manhattin distance between 2 points
    :param current: a tuple of x,y coordinates representing the current path
    :param goal: a tuple of x,y coordinates representing the end of path
    :return F: the number representing the mahattin distance"""

    x,y = current
    end_x,end_y = goal
    F = (end_x+end_y) - (x+y)
    return abs(F)



open_vertices = L.linked_list()

closed_vertices = []




def update_open_vertices(current,coordinate,open_vertices,end):
    """Purpose: to update the open_vertices list
    :param current: the current x,y coordinate we are trying to find the shortest path on
    :param coordinate: the x,y coordinate that is being considered as an open vertice
    :param open_vertices: a linked list representing the current open_vertices
    :param end: the goal we wish to reach"""

    f_value = distance_calculator(coordinate,end)
    if not open_vertices.value_is_in(coordinate):
        node = L.node(coordinate,f_value,current)
        open_vertices.insert(node)

    else:
        current_f = open_vertices.get_data(coordinate)

        if current_f > f_value:
            open_vertices.set_data(coordinate,f_value,current)
    


    



def get_open_vertices(current,grid,open_vertices,closed_vertices):
    '''Purpose: will grab new open vertices and add them to open_vertices list
    param current: the current position
    param grid: an nxm grid 
    param open_vertices: a linked_list storing open vertices
    '''
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
            elif (x,y) in closed_vertices:
                continue
            
            

                

    

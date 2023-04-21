



def distance_calculator(current,goal):
    """Purpose: calculates the manhattin distance between 2 points
    :param current: a tuple of x,y coordinates representing the current path
    :param goal: a tuple of x,y coordinates representing the end of path
    :return F: the number representing the mahattin distance"""

    x,y = current
    end_x,end_y = goal
    F = (end_x+end_y) - (x+y)
    return abs(F)

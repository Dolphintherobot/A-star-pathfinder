

class open_vertices:
    
    def __init__(self):
        """Purpose: to create a list of open vertices that stores a list of manhattin distance,
        coordinates and previous vertex"""

        self.__list = []

    
    def insert(self,distance,current,previous):
        ''''Purpose to insert a current vertex in ascending order with respect to distance
        :param distance: the distance from current vertex to the end of the grid
        :param current: a vertex on a graph represented by a tuple of x,y coordinates
        :param previous: the vertex on the graph by a tuple of x,y coordinates in which the distance was calculated from
        :Post-conditions: will update the list
        '''

        data = [distance,current,previous]
        i = 0
		
        while i < len(self.__list) and self.__list[i][0] < distance:
            i+=1
    
        self.__list.insert(i,data)


    def print_distance(self):
        """Purpose: a test function that is used to check to see if the f_values are in order"""


        for data in self.__list:
            print(data[0])

    def coordinate_is_in(self,distance,current,previous):
        ''''Purpose: will check to see if a current coordinate is in the list
        :param distance: the distance from current vertex to the end of the grid
        :param current: a vertex on a graph represented by a tuple of x,y coordinates
        :param previous: the vertex on the graph by a tuple of x,y coordinates in which the distance was calculated from
        :Post-conditions: will update the list
        :return: True if the value was found,False otherwise
        if current already exists in the list and has a lower distance it will be removed and reinserted

        '''

        for data in self.__list:
            if current == data[1]:
                if distance < data[0]:
                    self.__list.remove(data)
                    self.insert(distance,current,previous)
    
                return True

        return False

    def get_current(self):
        """Purpose will return the the vertex with the shortest manhattin distance
        :return vertex: tuple of x,y coordinates representing the shortest distance from end
        :Post-conditions: will cut remove the front of the list
        """

        vertex = self.__list[0][1]
        self.__list = self.__list[1:]
        return vertex 
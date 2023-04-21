class node:
    def __init__(self,coordinates=None,F_value=None,
    previous_value=None,next=None):
        '''Purpose: creates a node ADT'''
        self.coordinates = coordinates
        self.f_value = F_value
        self.previous_coordinates = previous_value
        self.next_node = next
    

class linked_list:
    def __init__(self):
        '''Purpose:creates a linked list'''
        self.head = None
        self.tail =None
        self.size = 0
    
    def length(self):
        '''Purpose:returns the length of the node chain
        :return size: an int representing the length of the chain'''
        return self.size
    
    def is_empty(self):
        '''Purpose:check if the list is empty
        :return:True if length is 0,false otherwise '''
        return self.size == 0

    def prepend(self,new_node:node):
        """Purpose:add a node to the front of the linked_list
        :param new_node: the node you wish to add to the list
        :return: None"""

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        self.size +=1


    def insert(self,new_node):
        """Purpose: add a new_node inside the list such that it keeps the F values in ascending order
        param new_node: a node class
        :return: None
        """

        if self.is_empty():
            self.size +=1
            self.head = new_node
            return 
        current = self.head
        
        while current.f_value > new_node.f_value and current != None:
            previous_node = current
            current = current.next_node
        
        previous_node.next = new_node
        new_node.next = current



    def remove_head(self):
        """Purpose:removes the head of the linked list and returns it's value
        :param new_node: the node you wish to add to the list
        :return: value, the coordinates inside the node"""

        assert self.size > 0, "removing from an empty list"
        the_node = self.head
        value = the_node.coordinates
        self.head = the_node.next_node

        self.size -=1

        if self.is_empty():
            self.head = None
            self.tail = None
        return value




    def remove_value(self,value:int):
        '''Purpose:removes a node at the specified index,note indexing starts at zero
        :param index: an int representing the nodes index you wish to remove
        :return: data,the node at the index, data'''

        if value == self.head.coordinates:
            return self.remove_head()
        
        current_node = self.head
        while current_node.coordinates != value and current_node != None:
            previous_node = current_node
            current_node = current_node.next_node
        

        if current_node == None:
            return False
        else:
            previous_node.next_node = current_node.next_node
            return True 
    


    def get_data(self,coordinates):

        '''Purpose:grabs the data of the node at the specified index,note this index starts at zero
        :param coordinates: tuple,representing the x,y cooridnates on the grid
        :return data: the F_value stored in the node'''

        
        i = 0
        current_node = self.head
        while coordinates != current_node.coordinates:
            current_node = current_node.next_node
            i+=1
        
        data = current_node.f_value
        return data

    def set_data(self,coordinates,f_value,previous_coordinates):
        '''Purpose:set the data of the node at the specified index,note this index starts at zero
        :param index: int, representing the index of the node you wish to grab
        :param value: the data you wish to store in the node at the index 
        :return: None '''

        
        
        current_node = self.head
        while coordinates != current_node.coordinates:
            current_node = current_node.next_node
            
        current_node.f_value = f_value
        current_node.previous_coordinates = previous_coordinates
        return None 
    

    def value_is_in(self,value):
        '''Purpose:checks to see if the value is stored in the list
        :param value: the value you wish to check
        :return: True if found, False otherwise'''
        
        found  = False
        current_node = self.head
        while current_node != None:
            if current_node.f_value == value:
                found = True
            current_node = current_node.next_node
        return found 
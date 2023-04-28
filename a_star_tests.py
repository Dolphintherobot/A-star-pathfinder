import a_star as A

import open_vertices as Ov


####################
#test distance calculator


current = (1,2)
goal =(4,5)

actual = A.distance_calculator(current,goal)
expected = 6
reason = "Checking manhattin distance"
if actual != expected:
    print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")




#test open_vertices class


a_list = Ov.open_vertices()

a_list.insert(20,"A","b")

a_list.insert(14,"A","b")
a_list.insert(199,"A","b")
a_list.insert(1,"A","b")

#a_list.print_distance()


#check when in order


a_list = Ov.open_vertices()

a_list.insert(1,"A","b")

a_list.insert(14,"A","b")
a_list.insert(199,"A","b")
a_list.insert(1000,"A","b")

#a_list.print_distance()





a_list = Ov.open_vertices()

a_list.insert(1,"A","b")


a_list.print_distance()

a_list.coordinate_is_in(14,"A","b")

a_list.print_distance()

a_list.coordinate_is_in(199,"A","b")

a_list.coordinate_is_in(-2,"A","b")
a_list.print_distance()



#test is_empty method

a_list = Ov.open_vertices()
test = "is_empty"
reason = "check empty list"
if not a_list.is_empty():
    print(f"error with {test} reason is {reason}")

a_list = Ov.open_vertices()
test = "is_empty"
reason = "check non empty list"
a_list.insert("A","a","A")
if a_list.is_empty():
    print(f"error with {test} reason is {reason}")






#################################
#test get_current method

a_list = Ov.open_vertices()

a_list.insert(1,"A","b")

a_list.insert(14,"a","b")
a_list.insert(199,"a","b")
a_list.insert(1000,"a","b")
check1 = a_list.get_current() == "A"
check2 = a_list.get_current() != "A"

if not (check1 and check2):
    print("error checking if get_current works")


##########################################################
#test square generator






def test_square_generator(dict):
    '''Purpose: to test the square_generator function
    :param dict: a dictionary containing the test cases,expected outputs and reasons for testing
    :return: None
    Post-conditions: will print error on console if expected !=actual output'''

    grid  = [[n for n in range(10)] for m in range(10)]
    for test in dict:
        current = test[0]
        taken = test[1]
        
        actual = A.square_generator(current,grid,taken)
        expected = dict[test][0]
        reason = dict[test][1]
        if actual != expected:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")



square_generator_tests = {
    #(current,taken):(expected,reason)
    ((5,4),()):([(4,3),(4,4),(4,5),(5,3),(5,4),(5,5),(6,3),(6,4),(6,5)],"check arbituary point"),
    ((-5,-4),()):([],"check out of bounds"),
    ((5,4),((4,3),(5,4))):([(4,4),(4,5),(5,3),(5,5),(6,3),(6,4),(6,5)],"check invalid spaces do not appear in list of valid points"),
}

test_square_generator(square_generator_tests)







def test_find_path(dict):
    '''Purpose: to test the find_path function
    :param dict: a dictionary containing the test cases,expected outputs and reasons for testing
    :return: None
    Post-conditions: will print error on console if expected !=actual output'''

    
    for test in dict:
        grid  = [[0 for n in range(10)] for m in range(10)]
        start = test[0]
        end = test[1]

        
        actual = A.find_path(grid,start,end)
        expected = dict[test][0]
        reason = dict[test][1]
        if actual != expected:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")




find_path_tests = {
    #(start,end):(expected,reason)
    ((0,0),(9,9)):(True,"check random grid with no blockades"),
    ((-4,-4),(9,9)):(False,"check out of bounds start"),
    ((9,9),(-4,-4)):(False,"check out of bounds end")

}

test_find_path(find_path_tests)






def test_find_path2(dict):
    '''Purpose: to test the find_path function,this time with walls involved
    :param dict: a dictionary containing the test cases,expected outputs and reasons for testing
    :return: None
    Post-conditions: will print error on console if expected !=actual output'''

    
    for test in dict:
        grid  = [[0 for n in range(10)] for m in range(10)]
        start = test[0]
        end = test[1]
        invalid_spaces = test[2]
        for space in invalid_spaces:
            x,y = space
            grid[x][y] = 2

        
        actual = A.find_path(grid,start,end)
        expected = dict[test][0]
        reason = dict[test][1]
        if actual != expected:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")


negative_diagonal = ((9,0),(8,1),(7,2),(6,3),(5,4),(4,5),(3,6),(2,7),(1,8),(0,9))
postive_diagonal = ((x,x) for x in range(10))
random_walls = ((5,5),(2,1),(5,6),(4,6),(1,6))

find_path_tests2 = {
    #(start,end,invalid_spaces):(expected,reason)
    ((0,0),(9,9),negative_diagonal):(False,"blocking off any possible entry to end"),
    ((0,0),(9,9),postive_diagonal):(False,"starting on a wall"),
    ((9,9),(0,0),random_walls):(True,"path open with walls blocking shortest path")

}

test_find_path2(find_path_tests2)




def test_find_path3(dict):
    '''Purpose: to test the find_path function,this time with a rectangular grid
    :param dict: a dictionary containing the test cases,expected outputs and reasons for testing
    :return: None
    Post-conditions: will print error on console if expected !=actual output'''

    
    for test in dict:
        grid  = [[0 for n in range(5)] for m in range(4)]
        
        start = test[0]
        end = test[1]
        invalid_spaces = test[2]
        for space in invalid_spaces:
            x,y = space
            
            grid[x][y] = 2
            
                


        
        actual = A.find_path(grid,start,end)
        expected = dict[test][0]
        reason = dict[test][1]
        if actual != expected:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")



negative_diagonal = ((0,4),(1,3),(2,2),(3,1))
postive_diagonal = ((x,x) for x in range(4))
random_walls = ((2,4),(2,1),(3,2),(1,1))

find_path_tests3 = {
    #(start,end,invalid_spaces):(expected,reason)
    ((0,0),(4,3),negative_diagonal):(False,"blocking off any possible entry to end"),
    ((0,0),(4,3),postive_diagonal):(False,"starting on a wall"),
    ((0,0),(3,4),random_walls):(True,"path open with walls blocking shortest path")

}


test_find_path3(find_path_tests3)
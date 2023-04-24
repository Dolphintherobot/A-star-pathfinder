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
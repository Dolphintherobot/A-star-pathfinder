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





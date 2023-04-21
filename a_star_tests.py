import a_star as A


import Llist as L


####################
#test distance calculator


current = (1,2)
goal =(4,5)

actual = A.distance_calculator(current,goal)
expected = 6
reason = "Checking manhattin distance"
if actual != expected:
    print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")





#########################
#test Linked list and node class


first = L.node((3,2),5,(3,4))
second = L.node((1,2),3,(3,4))
# print(first.f_value)
# print(second.coordinates)

L_list = L.linked_list()

L_list.insert(first)
L_list.insert(second)

check1 = L_list.remove_head() == second.coordinates
check2 = L_list.remove_head() == first.coordinates

reason = "Checking if insert keeps sorted based on heuristic distance"
if actual != expected:
    print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")
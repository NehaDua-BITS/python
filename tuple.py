""" Main difference between list and tuple is :
    Tuple is the list that can't be changed i.e. it is immutable
    But list can be converted to tuple and vice versa
"""

list1 = [1, 2, 3, 4, 5]
print(type(list1))

tuple1 = (1, 2, 3, 4, 5)
print(type(tuple1))
print(tuple1[3])
print(len(tuple1))

''' You can convert list to tuple and vice versa '''
newList = list(tuple1)
newList.append(20)
print(newList)
newTuple = tuple(newList)
print(newTuple)

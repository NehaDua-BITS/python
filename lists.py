#Lists are arrays in python

games = ["cricket", "badminton", "table tennis", "lawn tennis", "football"]
print("List of games are : {}".format(games))
print("3rd game is = " + games[3])
print("Last game is = " + games[-1])

print("type is : {}".format(type(games)))

mixedList = [10, "cricket", "badminton", "table tennis", 10.9]
print(type(mixedList))
print(mixedList[3])
print(mixedList[-3])

"""Advanced Operations"""
print("Advanced Operations : ")
mixedList.append(100)
mixedList.append("nick")
mixedList.append("cricket")
print(mixedList)
mixedList.insert(2, "chess")
mixedList.insert(0, "hello")
print(mixedList)
mixedList[1] = -40
print(mixedList)
del(mixedList[4])
print(mixedList)
""" Removes only 1st occurance of item """
mixedList.remove("cricket")
print(mixedList)

print("Length of list = {}".format(len(mixedList)))

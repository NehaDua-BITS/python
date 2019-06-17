''' Dictionaries are set of key-value pairs.
    Key is unique whereas value can be duplicate
    No insertion order of keys is maintained
'''

#Ignores duplicate keys; last pair overwrites the value
students = {"Anie" : 88, "James" : 67, "Sasha" :100, "Andry" : 78, "James" : 98,
            67 :"Bean"}
print(students)
print("Number of students = {}".format(len(students)))
print(students["Sasha"])
print(students[67])

''' Advanced Operations on Dictionaries '''
print("\nAdvanced Operations on Dictionaries")
print(students)
#insert
students["Neha"] = 99
print(students)
#update
students["Sasha"] = 55
print(students)
#delete
del(students[67])
print(students)

words = ["PoGo","Spange","Lie-Fi"]
definitions = ["Slang for Pokemon Go","To collect spare change, either from couches, passerbys on the street or any numerous other ways and means","When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]
cooldictionary = {}
for i in range(len(words)):
    cooldictionary[words[i]] = definitions[i]
print(cooldictionary)

print("Printing items (will print tuples) : ")
for item in students.items():
    print(item)

print("Printing keys : ")
print(students.keys())
for item in students.keys():
    print(item)

print("Printing values : ")
print(students.values())
for item in students.values():
    print(item)

print("Types : ")
print(type(students))
print(type(students.items()))
print(type(students.keys()))
print(type(students.values()))


''' keys are connected to dictionary but not list;
    list contains copy of elements '''
names = students.keys()
marks = students.values()
namesList = list(names)
print("Before Deletion : ")
print(names)
print(marks)
print(namesList)
print("After Deletion : ")
del(students["Sasha"])
print(names)
print(namesList)
print(marks)


dabools = [False, False, False, False, True, False, True, False, True, False, False, False, False, False, True, False, True, True, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, False, True, False, False, True, False, False, False, False, True, True, False, False, True, True, True, False, True, True, False, False, False, False, True, True, False, True, True, False, True, True, True, False, False, False, True, True, False, True, False, True, False, True, True, True, False, True, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, True, True, True, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, True, True, True, True, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, True, True, True, False, False, True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, True, True, True, False, True, False, False, True, False, False, True, True, False, False, False, False, True, False, False, True, True, False, True, True, False, False, True, False, True, True, False, True, False, True, False, True, False, False, True, False, True, False, False, False, True, True, False, False, False, True, True, False, False, True, True, True, True, True, False, True, True, True, True, False, False, True, False, True, True, True, True, True, False, False, False, True, True, False, True, True, True, False, False, True, True, False, True, True, True, True, False, True, True, False, False, False, True, True, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True, True, False, False, False, True, False, False, False, False, True, True, False, True, False, False, True, False, False, False, True, True, True, False, False, True, True, False, False, True, True, False, False, True, False, True, False, True, True, True, False, True, True, True, True, False, True, True, False, True, True, False, True, False, True, False, True, True, False, True, False, True, False, False, True, True, False, True, False, False, True, True, True, False, True, True, True, False, False, False, True, False, True, True, False, True, False, True, True, False, True, True, False, False, True, False, False, False, True, True, False, True, True, False, False, True, True, True, False, False, True, False, True, True, True, True, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True, True, False, False, False, True, False, False, True, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, True, False, True, True, False, False, True, False, False, True, True, False, True, False, True, False, False, True, False, True, True, False, False, True, True, False, False, True, False, False, False, False, True, False]

count = {}
for bool in dabools:
    if bool in count.keys():
        val = count[bool]
        count[bool] = val+1
    else:
        count[bool] = 1

print("Count is : ")
print(count)

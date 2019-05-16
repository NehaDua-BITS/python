print("hello world")
print('hello world')
#print("This is cool :emoji")  #this works with python 3 ctrl+command+space

#single line comment

""" multi line comment - use triple quotes single/double
this is interesting """

''' another way of multi line comment
this is also cool '''

commentStr = """** Multi line comments are nothing but simple strings **"""

print(commentStr)

string = ""'this is funny'""
print(str)

string = ''"this is funny''"
print(str)

string = '""this is funny""'
print(str)

string = "''this is funny''"
print(str)

"""this is good
this is funny"""

str1 = "this is good"
str2 = " this is awesome"
print(str1 + str2)

str1 = "this is good"
str2 = " this is awesome"
str1 += str2
print(str1)
print(str2)

print(30 * "hello")
print("\n")
print("world" * 30)

print(30 * "hello" + " neha!!")

print(30 * ("hello" + " neha!!"))

age = 18
area = 100.5
name = "Neha"
print("My age = {} and area = {} and name = {}".format(age, area, name))


"""String Methods """

str1 = "Neha dua"
print("lower case : " + str1.lower())
print("upper case : " + str1.upper())

str1 = "Neha dua"
str2 = str1.lower()
print("lower case string : " + str2 + " original string : " + str1)


str1 = "i am good" * 10
str2 = str1.replace("good", "bad")
print("Replaced string : " + str2 + " \noriginal string : " + str1)


print("Splitted string in list : ")
print(str1.split())
print("original string : \n" + str1)

str1 = "i am of long length"
print(len(str1))
age = 10
print("age is " + str(age))

'''access individual characters in strings'''
print(str1[0])
print(str1[4])
print(str1[8])

"""string slicing"""
str1 = "hello world!!"
print(str1[0:8])
print(str1[0:1])
print(str1[8:10])
print(str1[0:])
print(str1[2:-3])

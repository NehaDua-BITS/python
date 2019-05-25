''' Notes:
1. Whatever we take from input, it is changed into String  '''

age = input("Enter your age : ")
#Get type of variable
print("Type is : {}".format(type(age)))

if int(age) >= 18:
    print("You are allowed to watch this content : {}".format(age))
else:
    print("Grow up first kid!!!")

#typecast the value
num = int(input("Enter any number : "))
print(type(num))

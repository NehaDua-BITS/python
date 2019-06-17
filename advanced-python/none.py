''' None -
    to represent something is missing
    or something didn't happen
'''

str = None
print("String is : ", str)


def square(number):
    typeVal = type(number)
    if (typeVal==int or typeVal==float):
        return number * number
    return None

print(square(5))
print(square(4.0))
print(square("2"))

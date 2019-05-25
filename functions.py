def simpleFunc():
    print("This is a simple function")
    print("This is cool")

def funcWithParams(first, last, age):
    print("this is function with parameters : name = " + first + " " + last)
    print("age = {}".format(age))

def sum(num1, num2):
    return num1 + num2

simpleFunc()
funcWithParams("First", "Last", 18)
print("Sum of ints is : {}".format(sum(12, 10)))
print("String concat is : {}".format(sum("neha", "dua")))
print("Sum of floats is : {}".format(sum(1.1, 3.5)))


""" Handling reordering of args """
def printSentence(name, verb, noun):
    print(name + " was " + verb + " with " + noun)

printSentence(noun="Parth", name="Neha", verb="running");

""" Default args """
def usingDefault(name="Nick", noun="Shawn"):
    print(name + " loves " + noun)

usingDefault("Parth", "Neha")
usingDefault()
usingDefault("Aisha")

""" Var args """
def varArgsFunc(first, last="savjani", *varArgs):
    print("Name is : {}{}".format(first, last))
    print(varArgs)

varArgsFunc("neha", "dua", 1,2,3,"ashu",8.9)


""" return types -> but not that neccesary """
def sumAgain(num1, num2) -> int:
    return num1 + num2

print("sumAgain is : {}".format(sumAgain(5,4)))

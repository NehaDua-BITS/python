#Base class
class Dog:
    intro = "This is default intro for Dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Child class
class BullDog(Dog):
    "This is bulldog"

print(Dog.intro)
print(BullDog.intro)

dog1 = Dog("James", 10)
print(dog1.name)
bulldog1 = BullDog("Andy", 17)
print(bulldog1.name)

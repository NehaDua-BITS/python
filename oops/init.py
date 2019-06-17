''' this method is like constructor
    it is called everytime instance is created
    it has specific syntax
    we can have only 1 init function
'''

class Dog:
    intro = "This is default intro"
    def __init__(self, name, age):
        print("init() called")
        self.intro = "This is " + name
        self.name = name
        self.age = age

dog1 = Dog("James", 10)
print(dog1.intro)
print(dog1.age)
dog2 = Dog("Andy", 15)
print(dog2.intro)
print(dog2.age)
print(Dog.intro)

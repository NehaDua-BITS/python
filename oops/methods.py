''' There are instance methods and class methods
    Main difference between them is : instance method takes self as arg
'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Class method
    def bark():
        print("Bow Bow!!!")

    #instance method
    def barkNow(self):
        print("Bark Now : Bow Bow!!")

dog1 = Dog("James", 15)
''' invalid class method cant be accessed by instance'''
#dog1.bark()
''' valid '''
Dog.bark()
dog1.barkNow()

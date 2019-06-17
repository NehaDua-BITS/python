''' Classes have instance and class Variables
    Class vars:  are common for all
    instance vars: are specific to the instance
''''

class Student:
    print("hello student")
    info = "This is a student"

student1 = Student()
#Instance Variables
student1.name = "Neha"
student2 = Student()
student2.name = "Parth"
student3 = Student()
print("Instance variables : ")
print(student1.name)
print(student2.name)

print("\nTypes: ")
print(type(student1))
print(Student)

print("\nClass Variables")
print(student1.info)
print(student2.info)
print(student3.info)
print(Student.info)
student1.info = "This is my specific info"
print(student1.info) ''' this will not overwrite but create instance variable'''

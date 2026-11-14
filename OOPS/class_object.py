# 01 - Classes and Objects
# A class is a blueprint. An object is created from that blueprint.

class Car:
    pass

# Create objects  of the Car class
car1 = Car()
car2 = Car()

print("Car 1:", car1)
print("Car 2:", car2)
print("Are they the same object?", car1 is car2)

# A more useful class with an initializer
#__init__ == techinacilly initilazier || constructor
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Asha", "Computer Science")
student2 = Student("Ravi", "Information Technology")

print("\n", student1.name, "studies", student1.course)
print(student2.name, "studies", student2.course)

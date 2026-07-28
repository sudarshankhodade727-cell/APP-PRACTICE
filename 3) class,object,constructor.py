# Class
class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Object creation
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Calling the method
student1.display()
student2.display()

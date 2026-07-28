class Student:
    school = "ABC School"   # Class variable

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # 1. Instance Method
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    # 2. Class Method
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # 3. Static Method
    @staticmethod
    def greet():
        print("Welcome to the Student Management System")


# Create an object
s1 = Student("Alice", 95)

# Call Instance Method
s1.display()

# Call Class Method
Student.change_school("XYZ School")
print("School:", Student.school)

# Call Static Method
Student.greet()

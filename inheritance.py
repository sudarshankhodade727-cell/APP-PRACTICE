# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Create an object of the child class
dog1 = Dog()

# Call methods
dog1.eat()   # Inherited from Animal
dog1.bark()  # Defined in Dog

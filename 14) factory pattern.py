# Factory Pattern in Python

class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def get_animal(animal):
        if animal.lower() == "dog":
            return Dog()
        elif animal.lower() == "cat":
            return Cat()
        else:
            return None

# Main Program
choice = input("Enter animal (dog/cat): ")

animal = AnimalFactory.get_animal(choice)

if animal:
    print("Animal says:", animal.speak())
else:
    print("Invalid animal!")

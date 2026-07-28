# Liskov Substitution Principle (LSP)

from abc import ABC, abstractmethod

# Base class
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

# Sparrow class
class Sparrow(Bird):
    def move(self):
        print("Sparrow is flying.")

# Penguin class
class Penguin(Bird):
    def move(self):
        print("Penguin is swimming.")

# Function that works with any Bird
def bird_action(bird):
    bird.move()

# Main Program
sparrow = Sparrow()
penguin = Penguin()

bird_action(sparrow)
bird_action(penguin)

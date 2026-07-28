# ---------------- Singleton Pattern ----------------
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# ---------------- Factory Pattern ----------------
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

# ---------------- Observer Pattern ----------------
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print("Observer received:", message)

# ---------------- Strategy Pattern ----------------
class Add:
    def execute(self, a, b):
        return a + b

class Multiply:
    def execute(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)

# ---------------- Decorator Pattern ----------------
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

# ---------------- Main Program ----------------
print("=== Singleton Pattern ===")
obj1 = Singleton()
obj2 = Singleton()
print("Same object:", obj1 is obj2)

print("\n=== Factory Pattern ===")
animal = AnimalFactory.get_animal("dog")
print("Animal says:", animal.speak())

print("\n=== Observer Pattern ===")
subject = Subject()
obs1 = Observer()
obs2 = Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.notify("Welcome!")

print("\n=== Strategy Pattern ===")
calc = Calculator(Add())
print("Addition:", calc.calculate(10, 5))
calc = Calculator(Multiply())
print("Multiplication:", calc.calculate(10, 5))

print("\n=== Decorator Pattern ===")
greet()

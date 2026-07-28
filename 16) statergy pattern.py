# Strategy Pattern in Python

class Add:
    def execute(self, a, b):
        return a + b

class Subtract:
    def execute(self, a, b):
        return a - b

class Multiply:
    def execute(self, a, b):
        return a * b

class Calculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)

# Main Program
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")

choice = int(input("Enter your choice: "))

if choice == 1:
    calc = Calculator(Add())
elif choice == 2:
    calc = Calculator(Subtract())
elif choice == 3:
    calc = Calculator(Multiply())
else:
    print("Invalid choice")
    exit()

print("Result:", calc.calculate(a, b))

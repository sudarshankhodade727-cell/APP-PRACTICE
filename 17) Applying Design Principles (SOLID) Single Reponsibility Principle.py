# Single Responsibility Principle (SRP)

# Class responsible only for storing employee data
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Class responsible only for calculating salary
class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.salary

# Class responsible only for printing employee details
class EmployeePrinter:
    def print_details(self, employee):
        print("Employee Name:", employee.name)
        print("Employee Salary:", employee.salary)

# Main Program
emp = Employee("Sudarshan", 50000)

calculator = SalaryCalculator()
printer = EmployeePrinter()

printer.print_details(emp)
print("Calculated Salary:", calculator.calculate_salary(emp))

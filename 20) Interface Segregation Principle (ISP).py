# Interface Segregation Principle (ISP)

from abc import ABC, abstractmethod

# Interface for printing
class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

# Interface for scanning
class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Printer class only implements printing
class SimplePrinter(Printer):
    def print_document(self):
        print("Printing document...")

# Multi-function printer implements both interfaces
class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self):
        print("Printing document...")

    def scan_document(self):
        print("Scanning document...")

# Main Program
printer = SimplePrinter()
printer.print_document()

mfp = MultiFunctionPrinter()
mfp.print_document()
mfp.scan_document()

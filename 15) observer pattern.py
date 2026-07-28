# Observer Pattern in Python

class Observer:
    def update(self, message):
        print("Received:", message)

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

# Main Program
subject = Subject()

observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello Observers!")

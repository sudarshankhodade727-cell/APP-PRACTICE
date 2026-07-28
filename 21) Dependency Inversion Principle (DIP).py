# Dependency Inversion Principle (DIP)

from abc import ABC, abstractmethod

# Abstract class
class MessageService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

# Email service
class EmailService(MessageService):
    def send_message(self, message):
        print("Email:", message)

# SMS service
class SMSService(MessageService):
    def send_message(self, message):
        print("SMS:", message)

# High-level module
class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send_message(message)

# Main Program
email = EmailService()
sms = SMSService()

notification1 = Notification(email)
notification1.notify("Hello via Email!")

notification2 = Notification(sms)
notification2.notify("Hello via SMS!")

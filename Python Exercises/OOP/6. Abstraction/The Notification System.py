from abc import ABC, abstractmethod
class Notification(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailNotification(Notification):
    def send(self, recipient, message):
        return f"Sending Email To '{recipient}': {message}"

class SMSNotification(Notification):
    def send(self, recipient, message):
        return f"Sending SMS To '{recipient}': {message}"

email1 = EmailNotification()
phone1 = SMSNotification()
print(email1.send("esamv20@gmail.com", "Hi"))
print(phone1.send("01559600671", "Hi Again"))

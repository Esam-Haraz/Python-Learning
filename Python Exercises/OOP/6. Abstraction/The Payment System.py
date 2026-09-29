from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def __init__(self, user):
        self.user = user
    def process_payment(self, amount):
        return f"Processing Credit Card Payment Of {amount} for {self.user}"

class PayPalPayment(Payment):
    def __init__(self, user):
        self.user = user
    def process_payment(self, amount):
        return f"Processing PayPal Payment Of {amount} for {self.user}"

cc_user = CreditCardPayment("Esam")
print(cc_user.process_payment(1500))
pp_user = PayPalPayment("Nour")
print(pp_user.process_payment(2000))

class BankAccount:
    def __init__(self, client_name, initial_balance):
        self.client_name = client_name
        self.initial_balance = initial_balance
    def edit_balance(self, amount):
        self.initial_balance += amount
        return f"Deposit Successful!, {self.client_name}'s New Balance Is: {self.initial_balance}"

customer = BankAccount("Esam", 10000)
print(customer.edit_balance(5000))

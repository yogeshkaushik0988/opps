class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self._account_number = account_number  # Protected attribute
        self._balance = initial_balance       # Protected attribute

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example Usage
account = BankAccount("12345", 1000)
print(f"Current balance: {account.balance}")
account.deposit(500)
account.withdraw(200)
account.withdraw(1500) # Invalid withdrawal
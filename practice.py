class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute via name mangling

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # Output: 150

# Trying to access __balance directly will raise an AttributeError:
print(account.__balance)  # Uncommenting this will cause an error.

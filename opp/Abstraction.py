from abc import ABC,abstractmethod

# Abstrack BAse Class

class BankAccount(ABC):
    def __init__(self,account_number,account_holder):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=0

    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.interest_rate=0.05
    
    def deposite(self, amount):
        if amount > 0:
            self.balance+=amount
            print(f"Deposited ${amount}into saving account")
        else:
            print("invalid deposite amount")
    
    def withdraw(self, amount):
        if 0 <amount <=self.balance:
            self.balance-=amount
            print(f"withdrew ${amount} from samving account")

    def apply_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest
        print(f"Applied interest:${interest}")

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder):
        super().__init__(account_number, account_holder)
        self.overdraft_limit = 10000  # ₹10,000 overdraft

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount} into Current Account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ₹{amount} from Current Account.")
        else:
            print("Overdraft limit exceeded or invalid withdrawal amount.")


def display_account_details(account):
    print(f"\nAccount Holder:{account.account_number}")
    print(f"\nAccount Holder:{account.account_holder}")
    print(f"\nAccount balance:{account.get_balance()}")

savings = SavingsAccount("SA123", "Rohan AR")
current = CurrentAccount("CA456", "Sneha R")

savings.deposite(5000)
savings.withdraw(2000)
savings.apply_interest()


current.deposite(10000)
current.withdraw(15000)

display_account_details(savings)
display_account_details(current)












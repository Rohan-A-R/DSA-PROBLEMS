class BankAccount():
    def __init__(self,owner,balance):
        self.owner=owner
        self._account_number="123456789"
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def deposite(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f"deposited {amount}. New balance:{self.__balance}")
        else:
            print("invalid depossit amount")

    def withdraw(self,amount):
        if amount > 0  and amount < self.__balance:
            self.__balance -=amount
            print(f"withdraw {amount}. Remaining balance:{self.__balance}")

account=BankAccount("rohan",500)

print(account.owner)  #public

print(account._account_number)  # protected but not recomrndded

#using methods to modify private data

account.deposite(600)
account.withdraw(250)

        
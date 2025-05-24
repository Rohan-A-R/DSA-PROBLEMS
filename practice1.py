# class Solution:
#     def __init__(self,name,college):
#         self.name=name
#         self.college=college
#         self.total=200

#     def subject(self,subjects):
#         self.subjects=subjects
#         print(f'{self.name} is studing subjct {self.subjects} from {self.college}')

#     def mark(self,marks):
#         self.marks=(marks/self.total)*100
#         print(f'{self.name} is studing subjct {self.subjects} from {self.college} and socred {self.marks}')




# new=Solution('rohan','rv')
# new.subject('maths')
# new.mark(80)
# print(new.college)



# class Bank:
#     def __init__(self,balance=0):
#         self.balance=balance

#     def deposite(self,amount):
#         self.balance+=amount
#         print(f'the amount {amount} iss deposited and total balance is {self.balance}')

#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#         else:
#             print('insuffcient balnce')

#     def total(self):
#         print(f'total balance is {self.balance}')

# money=Bank()
# money.deposite(100)
# money.withdraw(50)
# money.total()
# money.withdraw(51)
# money.total()



# class Student:
#     def __init__(self,marks):
#         self.__marks=marks
#         self.__total=10

#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks*self.__total
#         else:
#             print('error')

#     def marks(self):
#         print(f'marks is {self.__marks}')



# marks=Student(100)
# marks.set_marks(100)
# marks.marks()
# print(marks.__marks)

# class Employee:
#     raise_amount=1.04
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay

# class Devloper(Employee):
#     raise_amount=1
#     def __init__(self, first, last, pay,programing):
#         super().__init__(first, last, pay)
#         self.prog=programing

#     def money(self):
#         self.pay=self.pay*Employee.raise_amount
#         print(f'{self.first + self.last} {self.prog} {self.pay}')


# emplo=Devloper('rohan','ar',100,'python')
# print(emplo.money())



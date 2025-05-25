class Solution:
    def __init__(self,name,college):
        self.name=name
        self.college=college
        self.total=200

    def subject(self,subjects):
        self.subjects=subjects
        print(f'{self.name} is studing subjct {self.subjects} from {self.college}')

    def mark(self,marks):
        self.marks=(marks/self.total)*100
        print(f'{self.name} is studing subjct {self.subjects} from {self.college} and socred {self.marks}')




new=Solution('rohan','rv')
new.subject('maths')
new.mark(80)
print(new.college)



class Bank:
    def __init__(self,balance=0):
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        print(f'the amount {amount} iss deposited and total balance is {self.balance}')

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print('insuffcient balnce')

    def total(self):
        print(f'total balance is {self.balance}')

money=Bank()
money.deposite(100)
money.withdraw(50)
money.total()
money.withdraw(51)
money.total()



class Student:
    def __init__(self,marks):
        self.__marks=marks
        self.__total=10

    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks*self.__total
        else:
            print('error')

    def marks(self):
        print(f'marks is {self.__marks}')



marks=Student(100)
marks.set_marks(100)
marks.marks()
print(marks.__marks)

class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

class Devloper(Employee):
    raise_amount=1
    def __init__(self, first, last, pay,programing):
        super().__init__(first, last, pay)
        self.prog=programing

    def money(self):
        self.pay=self.pay*Employee.raise_amount
        print(f'{self.first + self.last} {self.prog} {self.pay}')


emplo=Devloper('rohan','ar',100,'python')
print(emplo.money())


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_info(self):
        print(f'name{self.name}')
        print(f'age{self.age}')

class student(person):
    def __init__(self, name,age, grade):
        super().__init__(name, age)
        self.grade=grade

    def display_info(self):
        super().display_info()
        print(f'Student grade {self.grade}')
    
    def get_role(slef):
        return 'student'
    
class teacher(person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject

    def display_info(self):
        super().display_info()
        print(f'teacher subject {self.subject}')

    def get_role(self):
        return 'teacher'
    

student1=student('rohan',25,95)
student1.display_info()
print(student1.get_role())
teacher1=teacher('rama',45,'Maths')
teacher1.display_info()
print(teacher1.get_role())


class Animal:
    def speak(self):
        print('animal is speaking')


class Dog(Animal):
    def speak(self):
        print('dog is barking')

class Cat(Animal):
    pass

def poly(animal):
    animal.speak()


a=Dog()
b=Cat()

poly(a)
poly(b)


from abc import ABC,abstractmethod


class Payment(ABC):
    @abstractmethod
    def deposite(self):
        pass

    def withdraw(self):
        pass

class Debitcard(Payment):
    def __init__(self,name):
        self.name=name

    def deposite(self,amount):
        print(f'the amount {amount} is deopsited through debit card to {self.name}')

    def withdraw(self,amount):
        print(f'the amount {amount} is witdrawed through debit card to {self.name}')

class gpay(Payment):
    def __init__(self,upiId):
        self.upi=upiId

    def deposite(self,amount):
        print(f'the amount {amount} is deopsited through online card to {self.upi}')


debit=Debitcard('rohan')
debit.deposite(100)
debit.withdraw(100)
online=gpay('rohan ar')
online.deposite(100)
        
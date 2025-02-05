class Employee:
    raise_amt=1.04
    def __init__(self,first,last,pay):
        self.frst=first
        self.last=last
        self.email=first+'.'+last+'@email.com'
        self.pay=pay

    def fullname(self):
        return '{} {}'.format(self.frst,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):
    raise_amt=1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employess=None):
        super().__init__(first,last,pay)
        if employess is None:
            self.employess=[]
        else:
            self.employess=employess

    def add_emp(self,emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self,emp):
        if emp  in self.employess:
            self.employess.remove(emp)

    def print_emp(self):
        for emp in self.employess:
            print('-->',emp.fullname())
          




dev_1=Developer('rohan','ar',1000,'python')
dev_2=Developer('roith','s',1200,'java')


mgr_1=Manager('sue','smith',2000,[dev_1])


print(isinstance())

# print(mgr_1.email)
# mgr_1.add_emp(dev_2)

# mgr_1.print_emp()

# # print(dev_1.email)
# # print(dev_1.prog_lang)
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)
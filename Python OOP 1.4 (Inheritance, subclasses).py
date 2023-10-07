class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        #works too, useful when inheriting multiple classes
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
            
            
#Helps you to see all the inherited methods, variables etc.
#print(help(Developer))
        
dev_1 = Developer('Winfred','Cheok',50000,'Python')
dev_2 = Developer('Melvin','Lim',60000,'Java')

mgr_1 = Manager('Li','Fang',90000,[dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

#some usefule python functions
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)
# print(dev_1.pay)
# dev_1.apply_raise()
# #increases by developers 1.10 instead of the usual 1.04
# print(dev_1.pay)


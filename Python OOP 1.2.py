class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('Winfred','Cheok',50000)
emp_2 = Employee('Melvin','Lim',60000)

print(emp_1.__dict__)

print(emp_1.email)

#both syntax below are the same
print(emp_1.fullname())
print(Employee.fullname(emp_1))

#changes variable for all Employee instances
Employee.raise_amount = 1.05
#only changes variable for that specific instance of Employee
emp_1.raise_amount = 1.06

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)





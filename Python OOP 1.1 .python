class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
emp_1 = Employee('Winfred','Cheok',50000)
emp_2 = Employee('Melvin','Lim',60000)

print(emp_1.email)

#both syntax below are the same
print(emp_1.fullname())
print(Employee.fullname(emp_1))

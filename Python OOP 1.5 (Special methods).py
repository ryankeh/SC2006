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
    
    #for assisting developers to debug and work on code
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
        
        
    #for a readable piece of information
    # def __str__(self):
    #     pass

        
emp_1 = Employee('Winfred','Cheok',50000)
emp_2 = Employee('Melvin','Lim',60000)

print(emp_1)

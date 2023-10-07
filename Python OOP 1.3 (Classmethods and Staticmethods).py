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
        
    @classmethod
    def set_raise_amt(cls, amount):
        #cannot use class as a name cos is a keyterm used to declare classes
        cls.raise_amount=amount
    
    #alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

        
emp_1 = Employee('Winfred','Cheok',50000)
emp_2 = Employee('Melvin','Lim',60000)

#testing alternative constructor
emp_str_3 = 'Reyan-Thong-70000'
emp_3 = Employee.from_string(emp_str_3)
print(emp_3.__dict__)


Employee.set_raise_amt(1.05)
#can do with class or any instance of the class

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

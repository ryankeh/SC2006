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
    
    #the 2 methods below change how our objects are printed and displayed
    #for assisting developers to debug and work on code
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
    #for a readable piece of information
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    #used to define the "+" operand
    def __add__(self, other):
        return self.pay + other.pay
        
    def __len__(self):
        return len(self.fullname())

        
emp_1 = Employee('Winfred','Cheok',50000)
emp_2 = Employee('Melvin','Lim',60000)

# print(emp_1)
print(emp_1.__repr__())
print(emp_1.__str__())
#demonstrating the "__add__" method
print(emp_1 + emp_2)
#demonstrating the "__len__" method
print(len(emp_1))

#return(NotImplemented) at the bottom of the function will let the program fall back on the original function to see if it knows how to handle the operation

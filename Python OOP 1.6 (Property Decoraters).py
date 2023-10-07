#Getter, Setters and Deleters
class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    @property
    #allows us to access email as an attribute instead of a method, other code using our email attribute no need to change
    def email(self):
        return '{}.{}@e.ntu.edu.sg'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.First = None
        self.Last = None


        
emp_1 = Employee('Winfred','Cheok')
emp_2 = Employee('Melvin','Lim')

emp_1.first = "Losefred"
emp_1.fullname = 'Qi Wei'

#testing block
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)

del emp_1.fullname

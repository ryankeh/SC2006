#Saved in employee.py file
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Employee: {self.name}, Salary: ${self.salary}")

#Code in main.py file
# Import the Employee class from employee.py
from employee import Employee

# Create instances of the Employee class
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

# Use the class methods and attributes
employee1.display()
employee2.display()

#Run the following in command line to run main file
"python main.py"

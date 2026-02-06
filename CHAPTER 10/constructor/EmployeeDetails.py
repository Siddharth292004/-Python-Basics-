"""
Program to initialize two variables using constructor
🔹 Hint:
Pass two arguments
Use self.variable
"""


class Employee:

    def __init__(self,Name,salary):
        self.Name = Name
        self.salary= salary
    
    def display(self):
        print(f"Employee Name: {self.Name}\nSalary: {self.salary}")

obj = Employee("Siddharth",20000)
obj.display()

# Create a parent class Person and child class Employee.
#S Use super() to call parent constructor.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name,age)
        self.emp_id = emp_id

emp1 = Employee("Alice", 30, "E001")
print(f"Employee Name: {emp1.name}, Age: {emp1.age}, Employee ID: {emp1.emp_id}")
"""
Program to initialize student name using constructor

🔹 Hint:

Pass name as parameter

Use self.name

"""

class Student:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Student Name: {self.name}")

student1 = Student("Upendra singh ")
student1.display()
student2 = Student("Bob")
student2.display()
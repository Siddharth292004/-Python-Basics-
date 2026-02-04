"""
Use __init__() to initialize student name and roll number.
🔹 Hint:
Use constructor
Pass values while creating object
"""

class Student:
    def __intit__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

st1 = Student("Alice", 101)
st1.display()
st2 = Student("Bob", 102)
st2.display()
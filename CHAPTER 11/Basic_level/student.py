"""
Docstring for CHAPTER 11.Basic_level.student
Create a program using inheritance with any real-life example (Person → Student).
"""

class Person:
    
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo


class Student(Person):
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.rollNo}")

st = Student("Siddharth",101)
st.display()
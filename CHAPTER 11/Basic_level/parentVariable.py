"""
Docstring for CHAPTER 11.Basic_level.parentVariable
 Access Parent Variable from Child
Question:
Write a program where child class accesses a variable defined in parent class.
"""

class Parent:
    age = 30

class Child(Parent):
    def show_age(self):
        print("Age from parent class is:", self.age)

ch = Child()
ch.show_age()
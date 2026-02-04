
"""
Docstring for CHAPTER 11.Basic_level.exampleInheritance_02
Create a parent class with one method.
Child class should add a new method and call both.
"""

class Parent:
    def parent_message(self):
        print("Parent method called")

class Child (Parent):
    def child_message(self):
        print("Child method called")

ch1 = Child()
ch1.parent_message()
ch1.child_message()
"""
Docstring for CHAPTER 11.Intermidate_Level.overridingExample_01
Override a parent method in child class and still call parent method using super().
"""

class Parent:
    def display(self):
        print("Parent display")

class Child(Parent):
    def display(self):
        super().display()
        print("Child display")

ch = Child()
ch.display()
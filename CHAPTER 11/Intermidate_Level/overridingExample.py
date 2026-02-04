"""
Docstring for CHAPTER 11.Intermidate_Level.overridingExample
Write a program where child class overrides a parent method.
"""

class Parent:
    def message():
        print("This is Parent method")
    
class Child(Parent):
    def message(self):
        print("This is child method ")

ch = Child()
ch.message()
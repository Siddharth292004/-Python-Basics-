"""
Docstring for CHAPTER 11.Basic_level.exampleInheritance
Write a program where a child class inherits a method from a parent class and calls it.
"""

class Parent:
    def show_message(self):
        print("This is message for parent class")

class child (Parent):
    def childMethod(self):
        print("This message for child class")

ch = child()
ch.show_message()
ch.childMethod()


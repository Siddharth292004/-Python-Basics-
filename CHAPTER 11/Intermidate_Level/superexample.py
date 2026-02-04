"""
Docstring for CHAPTER 11.Intermidate_Level.superexample
Write a program where child class uses super() to call parent constructor.
"""

class Parent:
    def __init__(self):
        print("Parent Constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor called")
    
ch = Child()

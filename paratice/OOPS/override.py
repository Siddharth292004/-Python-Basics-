"""
Method overriding means the child class changes the behavior of a method of the parent class.

But sometimes we also want to use the parent class method.
So we use super() to call the parent method.
"""


class Parent:
    def display(self):
        print("This is the parent class Method")

class Child(Parent):
    def display(self):
        super().display()
        print("This is the child class Method")

child_obj = Child()
child_obj.display()
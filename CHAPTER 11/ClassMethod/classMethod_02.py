"""
Write a program where a @classmethod is called without creating an object.
"""

class Student:

    @classmethod
    def printMethod(cls):
        print("Class Method")

Student.printMethod()

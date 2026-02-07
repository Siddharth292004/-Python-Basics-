"""
Create a classs 'Pets' from a class 'Animal' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to
class 'Dog'.
"""

class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow Bow")

D = Dog()
D.bark()

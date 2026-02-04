"""
Docstring for CHAPTER 11.Intermidate_Level.MultipleInheritance
Write a program using two parent classes and one child class.
"""

class A:
    def methodA(self):
        print("Method from class A")

class B:
    def methodB(self):
        print("Method from class B")
    
class C(A,B):
    def methodC(self):
        print("Method from class C")


char = C()
char.methodA()
char.methodB()
char.methodC()
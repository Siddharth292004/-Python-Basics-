"""
Write a program using multilevel inheritance (A → B → C).
Hint 1:
Each class should inherit previous one.
Hint 2:
Call method of class A using object of C
"""

class A:
    def methodA(self):
        print("This is method of class A")

class B(A):
    def methodB(self):
        print("This is method of class B")

class C(B):
    def methodC(self):
        print("This is method of class C")

objC = C()
objC.methodA()  # Calling method of class A
objC.methodB()  # Calling method of class B
objC.methodC()  # Calling method of class C
"""
Create c class(2-D vector) and use it to create another class represting a 3-D vector.
"""

class TwoVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class ThreeVector(TwoVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoVector(5,2)
b = ThreeVector(6,2,3)

a.show()
b.show()

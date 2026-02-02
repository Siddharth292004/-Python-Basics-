"""
Program to calculate area of rectangle

🔹 Hint:

Pass length and breadth

Area = length × breadth
"""

class Rectangle:

    def __init__(self,length,breath):
        self.length = length
        self.breath = breath


    def area(self):
        area = self.length * self.breath
        return area




rect  = Rectangle(5,2)
area  = rect.area()
print(f"Area returned: {area}")

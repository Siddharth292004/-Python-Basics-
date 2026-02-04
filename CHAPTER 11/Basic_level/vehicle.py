"""
Create a parent class Vehicle with method start().
Create a child class Car and call start().
"""


class Vechicle:
    def start(self):
        print("Vechile started")

class Car (Vechicle):
    pass

c1 = Car()
c1.start()

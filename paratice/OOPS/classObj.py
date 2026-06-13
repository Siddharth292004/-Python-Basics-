# Create a class Car with attributes name and price. Create object and print values
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
car1 = Car("BMW", 50000)
car2 = Car("Audi", 60000)
print(f"Car 1: Name = {car1.name}, Price = {car1.price}")
print(f"Car 2: Name = {car2.name}, Price = {car2.price}")
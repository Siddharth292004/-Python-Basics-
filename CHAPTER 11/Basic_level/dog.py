class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")

# Object of child class
d = Dog()
d.sound()   # inherited method
d.bark()    # child class method

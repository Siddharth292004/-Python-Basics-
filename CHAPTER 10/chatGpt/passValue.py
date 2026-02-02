"""
5️⃣ Demonstrate use of self.

🔹 Hint:

Pass value using self.variable

Print it inside method

"""

class Person:
    def set_details(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

p1 = Person()
p1.set_details("Alice", 30)
p1.display()
p2 = Person()
p2.set_details("Bob", 25)
p2.display()
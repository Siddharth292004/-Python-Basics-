#Class Method as Alternative Constructor

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2026- birth_year)
    
p1 = Person("Alice", 30)
print(p1.name, p1.age)

p2 = Person.from_birth_year("Bob", 1990)
print(p2.name, p2.age)

print(p1.name, p1.age)



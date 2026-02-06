class Age:
    def __init__(self, age):
        self.age = age

    @property
    def get_age(self):
        return self.age

    @get_age.setter
    def set_age(self, age):
        if age < 0:
            print("Age cannot be negative.")
        else:
            self.age = age

a = Age(25)
print(a.get_age)  # getter
a.set_age = 30   # setter
print(a.get_age)
a.set_age = -5   # setter with invalid age
print(a.get_age)

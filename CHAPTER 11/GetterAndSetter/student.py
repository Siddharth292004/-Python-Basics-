class Student:
    def __init__(self, name):
        self._name = name   # protected variable

    # Getter
    def get_name(self):
        return self._name

    # Setter
    def set_name(self, name):
        self._name = name


s = Student("Rahul")

print(s.get_name())   # getter

s.set_name("Amit")    # setter
print(s.get_name())

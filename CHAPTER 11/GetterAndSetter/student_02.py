class Student:
    def __init__(self, name):
        self._name = name   # private variable

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if not name.strip():
            raise ValueError("Name cannot be empty!")
        self._name = name


s = Student("Siddharth")
print(s.name)
s.name = "Rahul"
print(s.name)
s.name =""
print(s.name)
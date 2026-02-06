class Person:
    sname = "Smith"

    @classmethod
    def change_sname(cls, new_sname):
        cls.sname = new_sname

    def display(self):
        print("Surname:", self.sname)

p = Person()
p.display()
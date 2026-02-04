class Student:
    Name = "ABC College"   # class variable

    @classmethod
    def change_name(cls, name):
        cls.Name = name    # modify class variable


Student.change_name("Marks University")
print(f"College Name: {Student.Name}")

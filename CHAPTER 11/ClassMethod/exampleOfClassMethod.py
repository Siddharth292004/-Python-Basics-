class Student:
    school = "ABC School"   # class variable

    @classmethod
    def change_school(cls):
        cls.school = "XYZ School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
Student.change_school()
Student.show_school()

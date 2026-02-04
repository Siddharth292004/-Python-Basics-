class Student:
    college = "ABC college"

    @classmethod
    def show_college(cls):
        print("College Name:",cls.college)
    

Student.show_college()


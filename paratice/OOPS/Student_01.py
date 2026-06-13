class Student:
    def __init__(self,):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks
    
    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            print("Marks cannot be negative.")

student1 = Student()
student1.marks = 85
print(student1.marks)
student1.marks = -10  # This will trigger the validation and print an error message

    
        
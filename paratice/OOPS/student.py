# Write a Python program to show student details using constructor.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_Student_detiails(self):
        print(f"Student Name : {self.name}")
        print(f"Student age : {self.age}")
        print(f"Student grade : {self.grade}\n")

st1  = Student( "John", 20, "A")
st2  = Student("Sid", 23, "Z")
st1.display_Student_detiails()
st2.display_Student_detiails()
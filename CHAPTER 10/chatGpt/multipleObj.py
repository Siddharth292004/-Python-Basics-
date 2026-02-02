"""
7️⃣ Create two objects and display different values.

🔹 Hint:

Use constructor

Create two objects with different data

🖥 Sample Output:
"""

class Student:
    def __init__(self, name, roll_number, age, class_name):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.class_name = class_name

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Age: {self.age}")
        print(f"Class: {self.class_name}")

st1 = Student("Upendra singh", 101, 25, "B.Tech")
st1.display()
st2 = Student("Siddharth singh ", 102, 24, "BBA")
st2.display()
st3 = Student("Jai sharma", 103,23, "MBA")
st3.display()
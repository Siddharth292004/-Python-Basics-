"""
7️⃣ Program to take user input inside constructor

🔹 Hint:

Use input() inside __init__()

Convert input if needed

"""


class Doctor: 

    def __init__(self):
        self.Name = input("Enter the Name: ")
        self.salary = input("Enter the salary: ")
    
    def display(self):
        print(f"Doctor Name : {self.Name}\nSalary: {self.salary}")

D1 = Doctor()
D1.display()
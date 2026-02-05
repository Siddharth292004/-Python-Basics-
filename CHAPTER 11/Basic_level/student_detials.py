class Student:
    def __init__(self,name,rollNo,branch):
        self.name = name
        self.rollNo = rollNo
        self.branch =branch


    def display(self):
        print(f"Name: {self.name}")
        print(f"RollNo: {self.rollNo}")
        print(f"Branch: {self.branch}\n")
        


st1 = Student("Siddharth",101,"CSE")
st2 = Student("Aman",101,"AI/ML")

st1.display()
st2.display()



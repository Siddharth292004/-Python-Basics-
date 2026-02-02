#3️⃣ Create a class with two variables and print them.

class SelfIntro:
    name = ""
    age  = 0

    def display(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")


s1 = SelfIntro()
s1.name = "siddharth"
s1.age = 23
s1.display()

"""
1️⃣ Create a class and an object, then print a message.
🔹 Hint:
Create a class
Define one method
Call method using object
"""


class Greeting:

    def display(self):
        print("Hello from class")


D1 = Greeting()
D1.display()



"""
self points to the current object that is using the class.
🔹 Why self is Used?
Python uses self to:
Connect object data with class methods
Store values inside a specific object
Tell Python “this variable belongs to this object”
👉 Without self, Python cannot know where to store the data
"""
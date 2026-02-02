#4️⃣ Create multiple objects of the same class.

#🔹 Hint:

#Create more than one object

#Call same method using different objects

#🖥 Sample Output:

#Object 1 called
#Object 2 called


class Sample:
    def display(self, object_number):
        print(f"Object {object_number} called")


obj1 = Sample()
obj2 = Sample()
obj3  =Sample()

obj1.display(1)
obj2.display(2)
obj3.display(3)
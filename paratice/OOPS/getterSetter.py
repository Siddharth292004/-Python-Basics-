"""
👉 Getter → Used to get (read) the value of a private variable.
👉 Setter → Used to set (update) the value of a private variable.

"""

class Student:
    def __init__(self, ):
        self.__name = "Rahul" 

     # Getter
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

student1 = Student()
student1.set_name("SIddharth")
print(student1.get_name())  
student1.set_name("Rahul")
print(student1.get_name())
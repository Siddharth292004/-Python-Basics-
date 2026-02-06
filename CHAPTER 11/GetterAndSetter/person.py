class Person:
    def __init__(self, Name, Age, gender, salary):
        self.Name = Name
        self.Age = Age
        self.gender = gender
        self.salary = salary


    def  get_name(self):
        return self.Name
   
    def get_Age(self):
        return self.Age
    
    def get_gender(self):
        return self.gender
    
    def get_salary(self):
        return self.salary
    
    
    def set_name(self, Name):
        self.Name = Name

    def set_Age(self, Age):
        self.Age = Age  

    def set_gender(self, gender):
        self.gender = gender

    def set_salary(self, salary):
        self.salary = salary
    

P1 = Person("Alice", 30, "Female", 50000)
print(P1.get_name())    # Getter
P1.set_salary(60000)     # Setter
P1.set_Age(34)
print(P1.get_Age())
P1.set_gender("Male")
print(P1.get_gender())
print(P1.get_salary())


def greet():
    print("Hello,siddharth")

greet()

# function with parameters

def greet1(name):
    print("Hello",name)

greet1("Rahul Sharma")


# function with multiple parameters


def add(a,b):
    return a + b

sum = add(10,12)
print(sum)


def greet2(name = "Guest"):
    print("Hello,",name)

greet2()
greet2("siddharth")

def student(name, age):
    print("Name: ",name)
    print("age: ", age)

student(age= 22,name ='siddharth')


# lambda function
# a lambda function is a small anonymous function

square = lambda x: x * x
print(square(5))



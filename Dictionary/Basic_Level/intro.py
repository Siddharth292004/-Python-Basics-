"""
A dictionary in Python is a collection of data in key-value pairs.
It is similar to a real-life dictionary, where each word (key) has a meaning (value).
👉 Python dictionaries are:
Ordered (from Python 3.7+)
Mutable (you can change values)
Do not allow duplicate keys
"""

student = {
    "Name": "Siddharth",
    "Age" : 22,
    "Course": "Python"
}

print(student)

# We use the key to access the value.

print(student["Age"])
print(student["Name"])
print(student["Course"])


# Adding New Element
student["City"] = 'jaipur'
print(student)

#Updating Value
student["Age"] = 50
print(student)

#Removing Elements
del student["Course"]
print(student)

# Looping through dictionary 
for key,value in student.items():
    print(key ,":" ,value)

students1 = {
    "s1": {"name": "Ram", "age": 20},
    "s2": {"name": "Shyam", "age": 21}
}

print(students1["s1"]["name"])


for key,value in students1.items():
    print(key,":",value)
student = {"name": "Siddharth", "age": 22, "city": "Jaipur"}

"""
1. keys() → Get all keys
👉 It returns all the keys in a dictionary.
"""
print(student.keys())
"""
values() → Get all values
👉 It returns all values in the dictionary.
"""
print(student.values())

"""
items() → Get key–value pairs
👉 It returns both key and value together.
"""

print(student.items())

"""
get() → Safe access
👉 It is safer than [] because it does not give an error if the key is not found.
"""
print(student.get("name"))
print(student.get("age"))
print(student.get("courese"))

"""
update() → Update dictionary
👉 It adds or updates values.
"""

student.update({"age": 23, "course": "Python"})
print(student)

"""
pop() → Remove element
👉 Removes the given key.
"""
student.pop("city")
print(student)


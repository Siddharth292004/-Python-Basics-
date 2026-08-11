
person = {
    "Name":"yono",
    "mob": 90543234543,
    "age" : 23,
    "education": "BTech",
    0: "gojo"
}

print(person)
print(person['Name'])
print(person['mob'])
print(person['education'])
print(person.keys())
print(person.values())
person.update({'age': 24,'Name': "Asta"})
print(person)
print(person.get('Name'))
print(person.get('education'))
print(person[0])

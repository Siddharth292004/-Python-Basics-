fruits = ['Apple','Banana']
fruits.append("CherrY")
print(fruits)


fruits.insert(1,"Mango")
print(fruits)


list1 = [1,2,3]
list2 = [4,5]

list1.extend(list2)
print(list1)


list1.remove(3)
print(list1)


list1.pop()
print(list1)

list1.clear()
print(list1)

print(fruits)

print(fruits.index("Banana"))


print(fruits.count("Banana"))

numbers = [1,2,3,4,5]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

new_list =numbers.copy()
print(new_list)

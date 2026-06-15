#A list in pythond is collection fo items stored in a single variable
#List can store multiple values
#List are ordered (items have postions/indexs).IndexError
#List are mutable (you can change, add ,or remove items)
#List can contain different data types

my_list = [10,20,30,40,50]

fruits = ["Apple","Banana", "mango"]
print(fruits)

# Accessing List Elements 
print(fruits[0])
print(fruits[1])
print(fruits[-1])
fruits[1] = "Orange"
print(fruits)

fruits.append("Grapes")
print(fruits)

fruits.insert(1,"Banana")

fruits.remove("Apple")
print(fruits)

fruits.pop()
print(fruits)


print(len(fruits))


numbers = [10,11,12,13,14,15] 
print(numbers[1:4])


for i in fruits:
    print( fruits)
    
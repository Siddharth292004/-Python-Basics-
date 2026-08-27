numbers = [10,20,30,40,50]

del numbers[2]
print("Updated list ",numbers)
del numbers[0:4]
print(numbers)

num = [1,2,3,4,5,6,7,8,9]

del num
# print(num)  # This will cause an error because numbers no longer exist

collection = ['Apple','Banana','cherry','date']

del collection[-1]
print(collection)

del collection[0:3]
print(collection)

del collection
# print(collection)  # This give also error and say collection is not define
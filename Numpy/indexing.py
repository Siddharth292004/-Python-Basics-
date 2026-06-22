import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Output: 10
print(arr[1])  # Output: 20
print(arr[2])  # Output: 30
print(arr[3])  # Output: 40
print(arr[4])  # Output: 50

print()
print(arr[-1])  # last element
print(arr[-2])  # second last
print(arr[-3])  # third last
print(arr[-4])  # fourth last
print(arr[-5])  # fifth last

print()

# slicing in 1D array

print(arr[1:4])    # from index 1 to 3
print(arr[:3])     # first three elements
print(arr[::2])    # every second element
print(arr[1::2])   # every second element starting from index 1
print(arr[::-1])   # reverse the array

# Indexing in 2D Array (Rows & Columns)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2[0, 0])  # Output: 1
print(arr2[0, 1])  # Output: 2
print(arr2[0, 2])  # Output: 3
print(arr2[1, 0])  # Output: 4
print(arr2[1, 1])  # Output: 5
print(arr2[1, 2])  # Output: 6
print(arr2[2, 0])  # Output: 7
print(arr2[2, 1])  # Output: 8
print(arr2[2, 2])  # Output: 9

# Access full row
print(arr2[1])

# Access full column
print(arr2[:, 1])




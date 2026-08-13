import numpy as np

my_array = np.array([[1,2],[3,4], [5,6],[7,8]],dtype=np.uint16)
print(my_array)

print("The shape of the array is: ",my_array.shape)
print("The number of dimensions of the array is: ",my_array.ndim)
print("The size of each element of the array is: ",my_array.itemsize)
print("Size of the array: ",my_array.size)
print("Type of the array is: ",my_array.dtype)


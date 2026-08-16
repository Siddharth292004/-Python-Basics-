import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D)

arr_3D = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(arr_3D)

arr_list = np.arange(1,10)
print(arr_list)
arr_ones = np.ones((2,3))
print(arr_ones)
arr_zeros = np.zeros((2,3))
print(arr_zeros)
arr_eye = np.eye((3))
print(arr_eye)
line_space = np.linspace(1,10,10)
print(line_space)


# numpy properties

arr2d = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2d.shape)
print(arr2d.ndim)
print(arr2d.dtype)
print(arr2d.size)
print(arr2d[-1])
print(arr2d[0,3])
print(arr2d[1,0])

a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])


print(a +b )
print(a - b)
print(a * b)
print(a /b)
print(a **b)

# comparsion operator

print(b >5)
print(b ==8)


# assingment operator

a+= 5
print(a)


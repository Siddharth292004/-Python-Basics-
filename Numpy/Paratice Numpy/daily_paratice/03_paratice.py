import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D)


arr_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr_3D)


arr_list = np.arange(1,10)
print(arr_list)

arr_list1 = np.arange(1,10,2)
print(arr_list1)

arr_ones = np.ones((2,3))
print(arr_ones)

arr_zeros = np.zeros((3,3))
print(arr_zeros)

arr_eye = np.eye((3))
print(arr_eye)

line_space = np.linspace(1,10,10)
print(line_space)



# numpy properties

arr2D = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2D.shape)
print(arr2D.ndim)
print(arr2D.dtype)
print(arr2D.size)
print(arr2D[-1])
print(arr2D[0,3])
print(arr2D[1,3])
print(arr2D[1,0])


a = np.array([1,2,3,4,5])
b = np.array([6,7,8,9,10])


print(a + b)
print(a - b)
print(a * b)
print(a / b)
print( a ** b)

# comparsion operator

print(b > 5)
print( b == 8)

# Bitwise operator 

c = np.array([1,2,3,4,5,6,7,8])
print( c << 1)
print( c >> 1)


# logical operator

print((c > 7 ) & (c < 10))
print(( c > 7 )  & (c == 8))
print(~(c))


# aggregation function

arr_2d = np.array([1,2,3,4,5,6,7])
print(np.sum(arr_2d))
print(np.min(arr_2d))
print(np.max(arr_2d))
print(np.sum(arr2D,axis=0))
print(np.sum(arr2D,axis=1))

print(np.min(arr2D,axis=1))
print(np.max(arr2D,axis=0))
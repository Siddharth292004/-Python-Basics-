import numpy as np


a = np.array([1, 2, 3, 4, 5])
b = np.array([6,7,8,9,10])
print(a + b)


c = np.array([[1,2],[3,4]])
d = np.array([[5,6],[7,8]])
print(c + d)
print(c - d)
print(c * d)
print(c / d)


e = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
f = np.array([[[9,10],[11,12]],[[13,14],[15,16]]])
print(e + f)

# array function

g = np.array([1, 2, 3, 4, 5])
print(g)


h = np.arange(10)
print(h)

i = np.zeros((3,2))
print(i)

j = np.ones((2,4))
print(j)

k = np.eye(4)
print(k)

l = np.linspace(0, 1, 5)
print(l)

m = np.random.rand(3,3)
print(m)


n = np.random.randint(1,10, size=(3,3))
print(n)


# array properties

arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.dtype)
print(arr_2d.itemsize)
print(arr_2d.nbytes)
print(arr_2d.T)  # transpose
print(arr_2d.flatten())  # flatten the array
print(arr_2d.reshape(3,2))  # reshape the array
print(arr_2d.reshape(3,2,1))  # reshape the array to 3D
print(arr_2d.reshape(1,6))  # reshape the array to 1D


# Operations on arrays

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 8, 9, 10])

print(np.add(x, y))
print(np.subtract(x, y))
print(np.multiply(x, y))
print(np.divide(y,x))
print(x **2)
print(y **2)


# comparsion

z = np.array([1,2,4,5,6])

print(z > 5)
print(z < 5)

# logical 
n = np.array([5,10,14])
o = np.array([7,8,9])

print((n > 5)&( n < 14))
print((n >5 ) | (n < 11))
print(~(o))

p = np.array([1,2,3,5])
r = np.array([2,4,6,8])
print(p << 1)
print(r >> 1)



q = np.array([1,3,4,5,6,7,8])
s = np.array([8,9,10,11,12,13,14])

print(np.subtract(q,s))
print(np.multiply(q,s))
print(np.divide(q,s))
print(np.add(q,s))
print(np.mean(q))
print(np.min(q))
print(np.max(q))
print(np.std(q))
print(np.var(q))
print(np.median(q))


arr = np.array([[1,2],[3,4]])

print(np.sum(arr))
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))


#  indexing and slicing

arr1 = np.array([1,2,3,4,5,6])

print(arr1[0])
print(arr1[1])
print(arr1[-1])

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(arr2[0,1])
print(arr2[1,2])


arr3 = np.array([1,2,3,4,5,6,7,7,8])
print(arr3[1:5])
print(arr3[:5])
print(arr3[::2])
print(arr3[::-1])
print(arr3[[0,2,4]])
print(arr3[arr3>3])

# reshape & modification

arr4 = np.array([1,2,3,4,5,6,7,8,9])
reshape_array = arr4.reshape(3,3)
print(reshape_array)

arr_2D = np.array([[1,2,3],[4,5,6]])
print(arr_2D.ravel())
print(arr_2D)
print(arr_2D.flatten())


# manipulatinga array


arr4 = np.array([1,2,3,4,5,6,7,8])
print(arr4)
new_array = np.insert(arr4,2,10)
print(new_array)

print(np.insert(arr4,3,12))


arr5 = np.array([10,20,30])
new_arr = np.append(arr5,[40,50,60])
print(new_arr)



arr6 = np.array([1,2,3,4,5])
arr7 = np.array([6,7,8,90,23])

new_array1 = np.concatenate((arr6,arr7))
print(new_array1)

print(np.delete(arr6,0))
import numpy as np

number = np.array([10,20,30,40])

print(number)

print(np.__version__)


arr = np.array([10,20,30,40,50])
print(arr)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)

arr4 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr4.shape)
print(arr4.ndim)
print(arr4.size)
print(arr4.dtype)


arr6 = np.array([1,2,3,4,5], dtype ='float64')
print(arr6)


# accesing array elements

arr7 = np.array([1,3,6,7,89,90,100])
print(arr7[0])
print(arr7[1])
print(arr7[2])
print(arr7[3])
print(arr7[4])
print(arr7[5])
print(arr7[6])



print(arr7[-1])
print(arr7[-2])
print(arr7[1:5])
print(arr7[1:5:2])


arr8 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr8[0,0])
print(arr8[1,2])


# math 

a = np.array([10,20,30,40])
b = np.array([1,2,3,4])

print(a+b)
print(a-b)
print(a * b)
print(a / b)

#  mathematical functions

arr9 = np.array([9, -2, 1, 2, 3, 4])

print(np.abs(arr9))
print(np.sqrt(arr9))
print(np.exp(arr9))
print(np.log(arr9))
print(np.log10(arr9))
print(np.log2(arr9))
print(np.sin(arr9))
print(np.cos(arr9))
print(np.tan(arr9))     
print(np.power(arr,2))
print(np.sum(arr9))
print(np.mean(arr9))
print(np.median(arr9))
print(np.std(arr9))
print(np.var(arr9))
print(np.min(arr9))
print(np.max(arr9))


arr10 = np.zeros((3,4))
print(arr10)

arr11 = np.ones((2,3))
print(arr11)

arr13 = np.arange(10)
print(arr13)


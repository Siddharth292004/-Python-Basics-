import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)


arrZero = np.array(80)
print(arrZero)

print(arr.ndim)
print(arrZero.ndim)

arr2 = np.array([[12,13,14],[16,17,18],[19,29,39]])
print(arr2)


print(arr.size)
print(arr2.size)


print(arr2.dtype)
arr3 = np.array([["String","Ram","jai"],["times","yoji","luffy"],["nike","system","jinwoo"]])
print(arr3)
print(arr3.dtype)

print(arr3.nbytes)
print(arr2.nbytes)
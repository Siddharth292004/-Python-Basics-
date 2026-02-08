"""
NumPy is a Python library used for working with numbers and arrays (lists of numbers) efficiently.
"""
from unittest import result
import numpy as np

a = np.array([1,2,3,5])
b = np.array([6,7,8,9])

result = a + b
print(result)  # take less more
print(a + b)

"""
short,fast,clean

"What is a NumPy Array?

A NumPy array is:

A special container to store numbers

Faster than Python list

All elements are of the same type 
"""

arr = np.array([10,20,30,40,50])
print(arr)


# 2D array example

matrix= np.array([[1,2,3],[3,4,5], [6,7,8]])

print(matrix)

arrMath = np.array([1,2,3,4])

print(arrMath + 5)
print(arrMath * 2)

   
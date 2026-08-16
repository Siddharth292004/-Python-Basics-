import numpy as np

arr = np.arange(1,17).reshape(4,4)
print("Original Array:\n", arr)

first_row = arr[0]
print("First Row:", first_row)

last_column = arr[:, -1]
print("Last Column:", last_column)

diagonal = np.diag(arr)
print("Diagonal:", diagonal)
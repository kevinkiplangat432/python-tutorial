import numpy as np

# Iterating through 1D array
arr1 = np.array([1, 2, 3, 4])
for x in arr1:
    print(x)

# Iterating through 2D array (row by row)
arr2 = np.array([[10, 20, 30], [40, 50, 60]])
for row in arr2:
    print("Row:", row)

# Iterating through every element in 2D
for row in arr2:
    for item in row:
        print(item)

# Using np.nditer for efficient iteration
arr3 = np.array([[1, 2], [3, 4]])
for x in np.nditer(arr3):
    print(x)

# Using ndenumerate to get index + value
for index, value in np.ndenumerate(arr3):
    print(index, value)

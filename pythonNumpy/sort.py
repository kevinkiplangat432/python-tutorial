import numpy as np

# Sorting 1D array
arr = np.array([5, 3, 8, 1])
sorted_arr = np.sort(arr)
print(sorted_arr)

# Sorting strings
str_arr = np.array(['banana', 'apple', 'cherry'])
print(np.sort(str_arr))

# Sorting booleans
bool_arr = np.array([True, False, True])
print(np.sort(bool_arr))

# Sorting 2D array row-wise
arr2 = np.array([[3, 1, 2], [9, 5, 4]])
print(np.sort(arr2))

# Sorting 2D array column-wise
print(np.sort(arr2, axis=0))

import numpy as np

# Splitting 1D array
arr = np.array([10, 20, 30, 40, 50, 60])
split_arr = np.array_split(arr, 3)  # 3 almost-equal parts
print(split_arr)

# Splitting 2D array row-wise
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
row_split = np.array_split(arr2, 3, axis=0)
print(row_split)

# Splitting 2D array column-wise
col_split = np.array_split(arr2, 2, axis=1)
print(col_split)

# Using hsplit specifically for columns
hs = np.hsplit(arr2, 2)
print(hs)

# Using vsplit for rows
vs = np.vsplit(arr2, 3)
print(vs)

# numpy indexing examples
import numpy as np

#getting the first element 
arr = np.array([1, 2, 3, 4])

print(arr[0])

#negative indexing
print(arr[-1])
print(arr[-2])


#2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0, 0])  # first row, first column
print(arr2d[1, 2])  # second row, third column
print(arr2d[2, 1])  # third row, second column
print(arr2d[-1, -1])  # last row, last column


#3D array indexing
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print(arr3d[0, 0, 0])  # first block, first row, first column
print(arr3d[1, 1, 1])  # second block, second row, second column
print(arr3d[2, 0, 1])  # third block, first row, second column
print(arr3d[-1, -1, -1])  # last block, last row, last column
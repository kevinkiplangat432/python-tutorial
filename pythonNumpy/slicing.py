#numpy slicing indecies examples
import numpy as np

#1D array slicing
arr1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("Original 1D array:", arr1d)  
print("Slicing from index 2 to 5:", arr1d[2:6])
print("Slicing with step 2:", arr1d[1:8:2])
print("Slicing till index 4:", arr1d[:5])
print("Slicing from index 4 to end:", arr1d[4:])    


#2D array slicing
arr2d = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])
print("\nOriginal 2D array:\n", arr2d)
print("Slicing rows 1 to 2 and columns 2 to 4:\n", arr2d[1:3, 2:5])
print("Slicing all rows and columns 1 to 3:\n", arr2d[:, 1:4])
print("Slicing rows 0 to 2 and all columns:\n", arr2d[0:3, :])
print("Slicing with step 2 in rows and columns:\n", arr2d[::2, ::2])    

#3D array slicing
arr3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                   [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                   [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print("\nOriginal 3D array:\n", arr3d)
print("Slicing first two blocks, all rows, and columns 1 to 2:\n", arr3d[0:2, :, 1:3])
print("Slicing all blocks, rows 1 to 2, and all columns:\n", arr3d[:, 1:3, :])
print("Slicing blocks 1 to end, all rows, and columns 0 to 1:\n", arr3d[1:, :, 0:2])
print("Slicing with step 2 in blocks, rows, and columns:\n", arr3d[::2, ::2, ::2])


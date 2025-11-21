import numpy as np

# 1. WHAT IS .shape ?
# .shape returns a tuple showing the size of the array
# in each dimension (rows, columns, depth, ...)

arr1 = np.array([1, 2, 3, 4])
print(arr1.shape)  
# (4,) → 1-dimensional array with 4 elements


# 2. SHAPE OF 2D ARRAYS (ROWS, COLUMNS)

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(arr2.shape)
# (2, 3) → 2 rows, 3 columns


# 3. SHAPE OF 3D ARRAYS
# In 3D: (depth, rows, columns)

arr3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],

    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr3.shape)
# (2, 2, 3)
# Meaning:
# - 2 blocks
# - each block has 2 rows
# - each row has 3 columns


# 4. CHECKING THE NUMBER OF DIMENSIONS (.ndim)
# .ndim tells you how many dimensions an array has

print(arr1.ndim)  # 1D
print(arr2.ndim)  # 2D
print(arr3.ndim)  # 3D


# 5. LENGTH OF EACH DIMENSION
# You can unpack shape to get the dimension sizes

rows, cols = arr2.shape
print("Rows:", rows)
print("Cols:", cols)

# For higher dimensions, unpack with more variables:
d, r, c = arr3.shape
print("Depth:", d)
print("Rows:", r)
print("Cols:", c)


# 6. USING len() WITH ARRAYS
# len(array) returns the size of the first dimension.
# Useful for iterating.

print(len(arr1))  # 4
print(len(arr2))  # 2 (because first dimension has 2 rows)
print(len(arr3))  # 2 (two blocks)


# 7. SHAPE OF ARRAYS CREATED WITH NUMPY FUNCTIONS
# These functions produce arrays with predictable shapes

zeros_arr = np.zeros((3, 4))
print(zeros_arr.shape)
# (3, 4)

ones_arr = np.ones((2, 2, 5))
print(ones_arr.shape)
# (2, 2, 5)

rand_arr = np.random.rand(6)
print(rand_arr.shape)
# (6,)


# 8. SHAPE OF SLICED ARRAYS
# Slicing can change the shape of the result

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

slice1 = a[:2]      # first 2 rows
print(slice1.shape) # (2, 3)

slice2 = a[:, 1:]   # all rows, columns 1 to end
print(slice2.shape) # (3, 2)

slice3 = a[0]       # first row
print(slice3.shape) # (3,) → becomes 1D array


# 9. EMPTY SHAPE FOR SCALARS
# NumPy scalars have shape = ()

scalar = np.array(42)
print(scalar.shape)
# () → means 0-dimensional
print(scalar.ndim)
# 0-dimensional array


# 10. AUTO-SHAPE BASED ON NESTED LIST STRUCTURE
# NumPy infers shape from how your Python lists are nested.

arr_nested = np.array([
    [ [1, 2], [3, 4] ],
    [ [5, 6], [7, 8] ],
])

print(arr_nested.shape)
# (2, 2, 2)
# 2 blocks → each with 2 rows → each row with 2 columns

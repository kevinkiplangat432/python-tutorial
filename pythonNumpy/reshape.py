import numpy as np

# 1. WHAT reshape() DOES
# reshape() changes the SHAPE of an array WITHOUT changing data.
# It returns a NEW array (usually a view, not a copy).

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_2x3 = arr.reshape(2, 3)

print(reshaped_2x3)
# [[1 2 3]
#  [4 5 6]]
print(reshaped_2x3.shape)   # (2, 3)


# 2. TOTAL ELEMENTS MUST MATCH
# You cannot reshape into a shape with a different number of elements.

# arr has 6 elements → valid reshapes: (1,6), (2,3), (3,2), (6,1)
# Reshape with inconsistent size throws an error:
# arr.reshape(4,4) → ERROR (because 16 elements needed)


# 3. USING -1 TO AUTO-CALCULATE DIMENSION
# NumPy auto-fills the -1 dimension based on total size.
# Only ONE -1 is allowed.

auto_rows = arr.reshape(-1, 3)  
print(auto_rows)
# Reshapes into (2, 3)

auto_cols = arr.reshape(2, -1)  
print(auto_cols)
# Reshapes into (2, 3)


# 4. WHEN reshape RETURNS A VIEW
# reshape usually returns a VIEW (shared memory), not a copy.
# But not always — depends on memory layout.

v = arr.reshape(2, 3)
print(v.base is arr)   # True → view (shared data)


# 5. MODIFYING THE RESHAPED VIEW CAN MODIFY ORIGINAL

v[0, 1] = 999
print("Original array:", arr)  
# Original changes because v is a view


# 6. RESHAPE TO HIGHER DIMENSIONS (3D, 4D, ...)

arr2 = np.arange(24)  # 0 to 23

cube = arr2.reshape(2, 3, 4)
print(cube.shape)
# (2 blocks, 3 rows, 4 columns)


# 7. FLATTENING AN ARRAY USING reshape
# reshape(-1) is a simple way to flatten arrays.

flat = cube.reshape(-1)
print(flat)
# [0 1 2 ... 23]


# 8. ORDER PARAMETER (ROW-MAJOR vs COLUMN-MAJOR)
# order='C' → row-major (default, reads rows first)
# order='F' → column-major (Fortran style, reads columns first)

arr3 = np.array([[1, 2], [3, 4]])

print(arr3.reshape(4, order='C'))  
# [1 2 3 4]

print(arr3.reshape(4, order='F'))  
# [1 3 2 4]
# Reads column-wise


# 9. RESHAPING DOES NOT CHANGE THE ORIGINAL ARRAY
# reshape() returns a new array (view/copy), original stays same.

original = np.array([10, 20, 30, 40])
new_shape = original.reshape(2, 2)

print(original.shape)  # (4,)
print(new_shape.shape) # (2, 2)


# 10. FORCE A COPY USING reshape(..., copy=True)
# Normally reshape tries to return a view.
# copy=True ensures a new independent array.

c = arr.reshape(2, 3, copy=True)
print(c.base)  # None → independent copy

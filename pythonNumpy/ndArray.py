import numpy as np

# creating a ndarray using array() function and a list
arr = np.array([[1, 2, 3,4, 5, 6]])
print("Original Array:", arr) 

print (type(arr))


#creating a ndarray using a tuple
arr2 = np.array((7, 8, 9,10,11,12))
print("Array from tuple:", arr2)
print (type(arr2))  


# 0-dimensional array
arr0d = np.array(42)
print("\n0-dimensional array:", arr0d)
print("Number of dimensions:", arr0d.ndim) 

# 1-dimensional array
arr1d = np.array([1, 2, 3, 4, 5])
print("\n1-dimensional array:", arr1d)
print("Number of dimensions:", arr1d.ndim)

# 2-dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-dimensional array:\n", arr2d)
print("Number of dimensions:", arr2d.ndim)

# 3-dimensional array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3-dimensional array:\n", arr3d)
print("Number of dimensions:", arr3d.ndim)

#higher dimensional array
arr4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
print("\n4-dimensional array:\n", arr4d)
print("Number of dimensions:", arr4d.ndim)  

# using ndmin to check dimensions
arr_ndmin = np.array([1, 2, 3, 4], ndmin=5)
print("\nArray with minimum 5 dimensions:\n", arr_ndmin)
print("Number of dimensions:", arr_ndmin.ndim)
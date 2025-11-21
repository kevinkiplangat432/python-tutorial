import numpy as np

# Basic filtering using a boolean list
arr = np.array([10, 25, 13, 40, 7])
filter_mask = [True, False, True, False, True]
filtered = arr[filter_mask]
print(filtered)

# Creating filters using conditions
greater_than_15 = arr[arr > 15]
print(greater_than_15)

even_numbers = arr[arr % 2 == 0]
print(even_numbers)

# Filtering 2D arrays
arr2 = np.array([[10, 3], [5, 20], [15, 8]])
filtered_2d = arr2[arr2 > 10]
print(filtered_2d)

# Multiple conditions
multi_filter = arr[(arr > 10) & (arr < 30)]
print(multi_filter)

import numpy as np

# Finding indexes where condition is true
arr = np.array([10, 20, 30, 40, 30, 20])
result = np.where(arr == 30)
print(result)  # indexes of 30

# Using condition inside where
greater_than_25 = np.where(arr > 25)
print(greater_than_25)

# Searching sorted arrays using searchsorted
sorted_arr = np.array([1, 3, 5, 7])
pos = np.searchsorted(sorted_arr, 4)
print(pos)  # where 4 should be inserted

# Using right side insertion
pos_right = np.searchsorted(sorted_arr, 4, side='right')
print(pos_right)

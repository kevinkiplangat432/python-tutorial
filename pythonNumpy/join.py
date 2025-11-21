import numpy as np

# Joining arrays using concatenate
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
joined = np.concatenate((a, b))
print(joined)

# Joining 2D arrays along rows
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
joined_rows = np.concatenate((x, y), axis=0)
print(joined_rows)

# Joining 2D arrays along columns
joined_cols = np.concatenate((x, y), axis=1)
print(joined_cols)

# Using stack (adds a new dimension)
stacked = np.stack((a, b), axis=0)
print(stacked)

# Using hstack (horizontal join)
h = np.hstack((a, b))
print(h)

# Using vstack (vertical join)
v = np.vstack((a, b))
print(v)

# Using dstack (depth join)
d = np.dstack((a, b))
print(d)

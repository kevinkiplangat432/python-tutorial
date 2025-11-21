import numpy as np

# 1. WHAT IS A VIEW?
# ------------------------------------------------------------
# A view is a new array that DOES NOT own the data.
# It only REFERENCES the same memory as the original array.
# Changing the view will change the original, and vice versa.

arr = np.array([10, 20, 30, 40])
view_arr = arr.view()   # Creates a view

print("Original:", arr)
print("View:", view_arr)
print("Do they share memory?", view_arr.base is arr)  
# True → view DOES NOT own the data


# 2. MODIFYING THE VIEW CHANGES THE ORIGINAL

view_arr[1] = 999
print("After modifying view:")
print("Original:", arr)   # Original changes
print("View:", view_arr)


# 3. SHAPE CHANGES IN A VIEW ALSO AFFECT ORIGINAL

arr2 = np.array([1, 2, 3, 4, 5, 6])
view2 = arr2.view()
view2.shape = (2, 3)

print("Original shape:", arr2.shape)   # Still (6,)
print("View shape:", view2.shape)      # (2, 3)
# Shape change DOES NOT affect original if it can't share layout.


# 4. WHAT IS A COPY?
# ------------------------------------------------------------
# A copy is a new array that OWNS its own data.
# Changing the copy DOES NOT affect the original.

arr3 = np.array([7, 8, 9])
copy_arr = arr3.copy()

print("Original:", arr3)
print("Copy:", copy_arr)
print("Do they share memory?", copy_arr.base is arr3)
# False → copy owns its own memory


# 5. MODIFYING THE COPY DOES NOT CHANGE THE ORIGINAL

copy_arr[0] = 9999
print("After modifying copy:")
print("Original:", arr3)
print("Copy:", copy_arr)


# 6. MEMORY RELATIONSHIP CHECK
# ------------------------------------------------------------
# .base → shows the parent array if it's a view

arr4 = np.array([100, 200, 300])
v = arr4.view()
c = arr4.copy()

print(v.base)  # Shows arr4 → means v is a view
print(c.base)  # None → means c is an independent copy


# 7. SLICING ALWAYS RETURNS A VIEW (NOT A COPY)

arr5 = np.array([10, 20, 30, 40, 50, 60])
slice_view = arr5[1:5]   # This is a view

slice_view[0] = 999
print("After modifying slice view:")
print("Original:", arr5)     # Affected
print("Slice View:", slice_view)


# 8. WHEN TO USE COPY() VS VIEW()
# ------------------------------------------------------------
# Use view() when:
#  - You want low-memory operations
#  - You want to manipulate the same underlying data
#
# Use copy() when:
#  - You want the original to remain unchanged
#  - You need safe data to modify independently


# 9. CHECKING IF AN ARRAY OWNS ITS DATA
# ------------------------------------------------------------
# flags['OWNDATA'] → True if array owns memory

x = np.array([1, 2, 3])
y = x.view()
z = x.copy()

print(x.flags['OWNDATA'])  # True
print(y.flags['OWNDATA'])  # False → view only references x
print(z.flags['OWNDATA'])  # True → independent memory


# 10. CHAINED VIEWS
# ------------------------------------------------------------
# A view created from another view still references the ORIGINAL

base = np.array([1, 2, 3, 4])
v1 = base.view()
v2 = v1.view()

v2[0] = 999
print("Base:", base)  # Modified
print("v1:", v1)
print("v2:", v2)
# All share the same data

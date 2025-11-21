import numpy as np

# 1. CHECKING DATA TYPES

arr = np.array([1, 2, 3])
print(arr.dtype)  
# dtype('int64') or dtype('int32') depending on your machine

# You can check the dtype of any NumPy object
print(np.dtype('float'))      # float64
print(np.dtype(np.int32))     # int32
print(np.dtype('bool'))       # bool

# 2. SPECIFYING DATA TYPES WHEN CREATING ARRAYS

arr_float = np.array([1, 2, 3], dtype='float32')
print(arr_float, arr_float.dtype)
# [1. 2. 3.] float32

arr_bool = np.array([0, 1, 2], dtype='bool')
print(arr_bool, arr_bool.dtype)
# [False  True  True] bool

arr_complex = np.array([1, 2, 3], dtype='complex128')
print(arr_complex, arr_complex.dtype)
# complex128

# 3. NUMPY DATA TYPE CATEGORIES

# Integers:
# int8, int16, int32, int64
a = np.array([10], dtype=np.int8)
print(a.dtype)

# Unsigned integers (no negative values):
# uint8, uint16, uint32, uint64
b = np.array([255], dtype=np.uint8)
print(b, b.dtype)

# Floats:
# float16, float32, float64
c = np.array([1.5], dtype=np.float16)
print(c, c.dtype)

# Complex numbers:
d = np.array([2 + 3j], dtype=np.complex64)
print(d, d.dtype)

# Boolean:
e = np.array([True, False], dtype=np.bool_)
print(e, e.dtype)

# Strings:
# NumPy stores strings with length limit, e.g. '<U5' means 5-char unicode
f = np.array(['Kevin', 'AI'], dtype='U5')
print(f, f.dtype)

# Bytes (fixed-length):
g = np.array([b'hi', b'hey'], dtype='S3')
print(g, g.dtype)

# 4. TYPE CASTING (astype)

arr = np.array([1.7, 2.3, 3.9])
arr_int = arr.astype('int32')
print(arr_int)
# Rounds DOWN because of truncation: [1 2 3]

arr_bool = arr.astype(bool)
print(arr_bool)
# All non-zero values become True: [True True True]

arr_str = arr.astype('U')
print(arr_str)
# ['1.7' '2.3' '3.9']

# ============================================================
# 5. TYPE PROMOTION (NumPy automatically chooses bigger type)
# ============================================================

# int + float → float
x = np.array([1], dtype=np.int32)
y = np.array([2.5], dtype=np.float32)
z = x + y
print(z, z.dtype)
# float32 or float64 depending on platform

# int + complex → complex
p = np.array([3], dtype=np.int32)
q = np.array([1 + 2j], dtype=np.complex64)
r = p + q
print(r, r.dtype)

# 6. TYPE INFORMATION HELPERS

print(np.iinfo(np.int32))  
# Shows min and max value of int32

print(np.finfo(np.float32))
# Shows float precision, min/max, eps, etc.

# 7. CHECKING IF TYPES ARE INTEGER/FLOAT/COMPLEX

arr1 = np.array([1, 2, 3.0])
print(arr1.dtype.kind)
# 'f' means float (other codes: i=int, u=unsigned, b=bool, c=complex, U=string)

# kind codes:
# i -> signed integer
# u -> unsigned integer
# f -> floating
# c -> complex
# b -> boolean
# U -> unicode string
# S -> byte string
# O -> Python objects

# Quick checks:
print(np.issubdtype(arr1.dtype, np.integer)) # False
print(np.issubdtype(arr1.dtype, np.floating)) # True
print(np.issubdtype(arr1.dtype, np.number))   # True

# 8. OBJECT DATA TYPE (SLOW, AVOID UNLESS NECESSARY)

# dtype=object lets you store ANY Python object
arr_obj = np.array([1, "Kevin", 3.14, True], dtype=object)
print(arr_obj, arr_obj.dtype)

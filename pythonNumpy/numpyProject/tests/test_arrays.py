# tests/test_analyzer.py

import numpy as np
import pytest
from analyzer import ArrayAnalyzer

an = ArrayAnalyzer()

# -------- CREATE ARRAY --------

def test_create_basic_array():
    arr = an.create_array([1, 2, 3])
    assert isinstance(arr, np.ndarray)
    assert arr.tolist() == [1, 2, 3]

def test_create_array_with_dtype():
    arr = an.create_array([1, 2], dtype="float32")
    assert arr.dtype == np.float32

def test_create_array_2d():
    arr = an.create_array([[1, 2], [3, 4]])
    assert arr.shape == (2, 2)


# -------- INDEXING --------

def test_get_element_valid():
    arr = np.array([10, 20, 30])
    assert an.get_element(arr, 1) == 20

def test_get_element_negative_index():
    arr = np.array([10, 20, 30])
    assert an.get_element(arr, -1) == 30

def test_get_element_2d():
    arr = np.array([[5, 6], [7, 8]])
    assert an.get_element(arr, (1, 0)) == 7


# -------- SLICING --------

def test_slice_basic():
    arr = np.array([1, 2, 3, 4, 5])
    assert an.slice_array(arr, 1, 4).tolist() == [2, 3, 4]

def test_slice_start_only():
    arr = np.array([1, 2, 3])
    assert an.slice_array(arr, 1).tolist() == [2, 3]

def test_slice_end_only():
    arr = np.array([1, 2, 3])
    assert an.slice_array(arr, end=2).tolist() == [1, 2]


# -------- DATATYPES --------

def test_get_dtype():
    arr = np.array([1, 2, 3], dtype="int32")
    assert an.get_dtype(arr) == np.int32

def test_cast_dtype():
    arr = np.array([1, 2, 3])
    out = an.cast_dtype(arr, "float64")
    assert out.dtype == np.float64


# -------- COPY vs VIEW --------

def test_make_copy_independence():
    arr = np.array([1, 2, 3])
    c = an.make_copy(arr)
    arr[0] = 99
    assert c[0] == 1

def test_make_view_linked():
    arr = np.array([1, 2, 3])
    v = an.make_view(arr)
    arr[0] = 50
    assert v[0] == 50

def test_copy_is_not_view():
    arr = np.array([1, 2, 3])
    assert an.make_copy(arr).base is None


# -------- SHAPE / RESHAPE --------

def test_get_shape():
    arr = np.array([[1, 2], [3, 4]])
    assert an.get_shape(arr) == (2, 2)

def test_reshape_array():
    arr = np.array([1, 2, 3, 4])
    reshaped = an.reshape_array(arr, (2, 2))
    assert reshaped.shape == (2, 2)

def test_reshape_validity():
    arr = np.arange(6)
    reshaped = an.reshape_array(arr, (3, 2))
    assert reshaped.tolist() == [[0, 1], [2, 3], [4, 5]]


# -------- ITERATING --------

def test_iterate_flat():
    arr = np.array([[1, 2], [3, 4]])
    assert an.iterate_array(arr) == [1, 2, 3, 4]

def test_iterate_1d():
    arr = np.array([10, 20, 30])
    assert an.iterate_array(arr) == [10, 20, 30]


# -------- JOIN --------

def test_join_vertical():
    a = np.array([1, 2])
    b = np.array([3, 4])
    out = an.join_arrays(a, b)
    assert out.tolist() == [1, 2, 3, 4]

def test_join_axis_1():
    a = np.array([[1, 2]])
    b = np.array([[3, 4]])
    out = an.join_arrays(a, b, axis=0)
    assert out.tolist() == [[1, 2], [3, 4]]


# -------- SPLIT --------

def test_split_array_even():
    arr = np.array([1, 2, 3, 4])
    a, b = an.split_array(arr, 2)
    assert a.tolist() == [1, 2]
    assert b.tolist() == [3, 4]

def test_split_array_3_parts():
    arr = np.array([1, 2, 3, 4, 5, 6])
    parts = an.split_array(arr, 3)
    assert [p.tolist() for p in parts] == [[1,2], [3,4], [5,6]]


# -------- SEARCH --------

def test_search_value_single():
    arr = np.array([1, 2, 3, 2])
    idx = an.search_value(arr, 2)
    assert idx.tolist() == [1, 3]

def test_search_value_none():
    arr = np.array([1, 2, 3])
    idx = an.search_value(arr, 99)
    assert idx.size == 0


# -------- SORT --------

def test_sort_ascending():
    arr = np.array([3, 1, 2])
    out = an.sort_array(arr)
    assert out.tolist() == [1, 2, 3]

def test_sort_2d_along_axis():
    arr = np.array([[3, 2, 1], [6, 5, 4]])
    out = an.sort_array(arr)
    assert out.tolist() == [[1, 2, 3], [4, 5, 6]]


# -------- FILTER --------

def test_filter_greater_than():
    arr = np.array([1, 5, 10, 2])
    out = an.filter_array(arr, lambda x: x > 3)
    assert out.tolist() == [5, 10]

def test_filter_even_numbers():
    arr = np.array([1, 2, 3, 4, 5])
    out = an.filter_array(arr, lambda x: x % 2 == 0)
    assert out.tolist() == [2, 4]

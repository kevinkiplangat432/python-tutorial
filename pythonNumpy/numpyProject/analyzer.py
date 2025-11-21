# analyzer.py
import numpy as np

class ArrayAnalyzer:
    """Utility class for analyzing numeric arrays using NumPy."""

    def create_array(self, data, dtype=None):
        """Return a numpy array from python data."""
        arr = np.array(data, dtype=dtype)
        return arr
        pass

    def get_element(self, arr, index):
        """Return element at index using numpy indexing."""
        return arr[index]
        pass

    def slice_array(self, arr, start=None, end=None):
        """Return slice of array from start to end."""
        return arr[start:end]
        pass

    def get_dtype(self, arr):
        """Return numpy dtype of array."""
        return arr.dtype
        pass

    def cast_dtype(self, arr, dtype):
        """Cast array to another dtype."""
        return arr.astype(dtype)
        pass

    def make_copy(self, arr):
        """Return a deep copy of the array."""
        return arr.copy()
        pass

    def make_view(self, arr):
        """Return a view of the array."""
        return arr.view()
        pass

    def get_shape(self, arr):
        """Return shape of array."""
        return arr.shape
        pass

    def reshape_array(self, arr, new_shape):
        """Return reshaped array."""
        return arr.reshape(new_shape)
        pass

    def iterate_array(self, arr):
        """Return list of elements by iterating."""
        return [x for x in np.nditer(arr)]
        pass

    def join_arrays(self, a, b, axis=0):
        """Join arrays along axis."""
        return np.concatenate((a, b), axis=axis)
        pass

    def split_array(self, arr, sections):
        """Split array into equal sections."""
        return np.array_split(arr, sections)
        pass

    def search_value(self, arr, value):
        """Return indices where value occurs."""
        return np.where(arr == value)[0]
        pass

    def sort_array(self, arr):
        """Return a sorted version of array."""
        return np.sort(arr)
        pass

    def filter_array(self, arr, condition_func):
        """
        Filter values using a condition function.
        condition_func receives the array and returns a boolean mask.
        """
        mask = condition_func(arr)
        return arr[mask]

        pass

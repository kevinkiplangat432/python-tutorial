#  a random number in numpy means sth that cannont be predicted
# random numbers generated using a generation algo is called pseudorandom numbers.
# they are not truly random because they are generated using a deterministic process.
# however, they can be used in simulations, cryptography, and statistical sampling where true randomness is not required.

import numpy as np
from numpy import random
def generate_random_numbers():
    # Generate a random float between 0 and 1
    rand_float = random.rand()
    print(f"Random float between 0 and 1: {rand_float}")

    # Generate an array of 5 random floats between 0 and 1
    rand_array = random.rand(5)
    print(f"Array of 5 random floats between 0 and 1: {rand_array}")

    # Generate a 2x3 array of random floats between 0 and 1
    rand_2d_array = random.rand(2, 3)
    print(f"2x3 array of random floats between 0 and 1:\n{rand_2d_array}")

    # Generate random integers between 10 and 50
    rand_int = random.randint(10, 50)
    print(f"Random integer between 10 and 50: {rand_int}")

    # Generate an array of 5 random integers between 10 and 50
    rand_int_array = random.randint(10, 50, size=5)
    print(f"Array of 5 random integers between 10 and 50: {rand_int_array}")

    # Generate a 2x3 array of random integers between 10 and 50
    rand_int_2d_array = random.randint(10, 50, size=(2, 3))
    print(f"2x3 array of random integers between 10 and 50:\n{rand_int_2d_array}")

    # Generate random numbers from a normal distribution (mean=0, std=1)
    rand_normal = random.normal(0, 1, size=5)
    print(f"Array of 5 random numbers from a normal distribution (mean=0, std=1): {rand_normal}")
    # Generate random numbers from a uniform distribution between 0 and 1
    rand_uniform = random.uniform(0, 1, size=5)
    print(f"Array of 5 random numbers from a uniform distribution between 0 and 1: {rand_uniform}")
    # Generate random numbers from a binomial distribution (n=10, p=0.5)
    rand_binomial = random.binomial(10, 0.5, size=5)
    print(f"Array of 5 random numbers from a binomial distribution (n=10, p=0.5): {rand_binomial}")
    #using rand() function to generate random numbers
    rand_nums = random.rand(3, 4)
    print(f"3x4 array of random numbers using rand():\n{rand_nums}")       
    #using choice() function to generate random samples from a given 1-D array
    sample_array = np.array([10, 20, 30, 40, 50])
    rand_samples = random.choice(sample_array, size=3, replace=False)
    print(f"Random samples from the array {sample_array}: {rand_samples}")  
if __name__ == "__main__":
    generate_random_numbers()
class NumpyAnalyzer:
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
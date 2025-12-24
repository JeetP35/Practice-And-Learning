import numpy as np

# Single-dimensional array
array1 = np.array([10, 20, 30, 40, 50])
print("Single-dimensional array:\n\n", array1 ,"\n")
print(type(array1))

# Multi-dimensional array
array2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Multi-dimensional array:\n\n", array2 ,"\n")
print(type(array2))

# Array of zeros
zeros_array = np.zeros((3, 4))
print("Array of zeros:\n\n", zeros_array ,"\n")

# Array of ones
ones_array = np.ones((2, 5))
print("Array of ones:\n\n", ones_array ,"\n")

# Array of a specific value
full_array = np.full((3, 3), 7)
print("Array of a specific value:\n\n", full_array ,"\n")

# Array with a specific range
range_array = np.arange(0, 20, 2)
print("Array with a specific range:\n\n", range_array ,"\n")

# Array with Random values
random_array = np.random.rand(4, 4)
print("Array with Random values:\n\n", random_array ,"\n")
# Gives any 4x4 array with random values between 0 and 1

# OR

random_int_array = np.random.randint(1, 100, 3)
print("Array with Random Integer values:\n\n", random_int_array ,"\n")
# Gives 3 random integers between 1 and 100
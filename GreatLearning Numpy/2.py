import numpy as np

# Shapes
array = np.array([[1, 2, 3], [4, 5, 6]])
array_shape = array.shape
print("Array:\n\n", array ,"\n")
print("Shape of the array:", array_shape ,"\n")

# Reshaping
reshaped_array = array.reshape(3, 2)
print("Reshaped Array (3x2):\n\n", reshaped_array ,"\n")

# OR

array.shape = (2, 3)
print("Reshaped Array using shape attribute (3x2):\n\n", array ,"\n")

# Stacking
# Vertical Stacking
npArray1 = np.array([1, 2, 3])
npArray2 = np.array([7, 8, 9])
v_stacked_array = np.vstack((npArray1, npArray2))
print("Vertically Stacked Array:\n\n", v_stacked_array ,"\n")

# Horizontal Stacking
h_stacked_array = np.hstack((npArray1, npArray2))
print("Horizontally Stacked Array:\n\n", h_stacked_array ,"\n")

# Column Stacking
col_stacked_array = np.column_stack((npArray1, npArray2))
print("Column Stacked Array:\n\n", col_stacked_array ,"\n")

# Intersection and Difference
arrayA = np.array([1, 2, 3, 4, 5])
arrayB = np.array([4, 5, 6, 7, 8])

# Intersection
intersection_array = np.intersect1d(arrayA, arrayB)
print("Intersection of arrayA and arrayB:\n\n", intersection_array ,"\n")

# Difference
difference_arrayAB = np.setdiff1d(arrayA, arrayB)
print("Difference of arrayA and arrayB (elements in arrayA not in arrayB):\n\n", difference_arrayAB ,"\n")

difference_array_BA = np.setdiff1d(arrayB, arrayA)
print("Difference of arrayB and arrayA (elements in arrayB not in arrayA):\n\n", difference_array_BA ,"\n")


import numpy as np

#Simple Maths with numpy arrays
arrayA = np.array([1, 2])
arrayB = np.array([7, 8])

# Addition
print(np.sum([arrayA, arrayB])) # Total sum

print(np.add(arrayA, arrayB)) # Sum along columns

# OR

print(np.sum([arrayA, arrayB], axis=0))  # Sum along columns
print(np.sum([arrayA, arrayB], axis=1))  # Sum along rows

# Basic Addition
arrayA += 1
arrayB += 2
print(arrayA)
print(arrayB)

# Basic Subtraction
arrayA -= 2
arrayB -= 1
print(arrayA)
print(arrayB)

# Basic Multiplication
arrayA *= 2
arrayB *= 3
print(arrayA)
print(arrayB)

# Basic Division
arrayA = arrayA / 2
arrayB = arrayB / 3
print(arrayA)
print(arrayB)

# Mean
arrayC = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(arrayC))          # Overall mean
print(np.mean(arrayC, axis=0))  # Mean along columns
print(np.mean(arrayC, axis=1))  # Mean along rows

# Median
arrayD = np.array([[10, 7, 4], [3, 2, 1]])
print(np.median(arrayD))          # Overall median
print(np.median(arrayD, axis=0))  # Median along columns
print(np.median(arrayD, axis=1))  # Median along rows

# Standard Deviation
arrayE = np.array([[1, 2, 3], [4, 5, 6]])
print(np.std(arrayE))          # Overall standard deviation
print(np.std(arrayE, axis=0))  # Standard deviation along columns
print(np.std(arrayE, axis=1))  # Standard deviation along rows
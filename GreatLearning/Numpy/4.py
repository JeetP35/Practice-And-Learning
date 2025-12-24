import numpy as np

# Matrix
matrixA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrixA[0]) # First row
print(matrixA[1]) # Second row
print(matrixA[2]) # Third row
print(matrixA[:, 0]) # First column
print(matrixA[:, 1]) # Second column
print(matrixA[:, 2]) # Third column
print(matrixA[1, 2]) # Element at row 2, column 3
print(matrixA[1, :])  # Row 2, all columns

# Transpose
print(np.transpose(matrixA)) # All rows and columns swapped

# Matrix Multiplication
matrixB = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrixA.dot(matrixB)) # Matrix A multiplied by Matrix B
print(matrixB.dot(matrixA)) # Matrix B multiplied by Matrix A
# Both give different results

# Save and Load
np.save('matrixA.npy', matrixA) # Save matrixA to a file
loadedMatrixA = np.load('matrixA.npy') # Load matrixA from the file
print(loadedMatrixA) # Display loaded matrixA
def matrix_addition(A, B):
    # Get the dimensions of the matrices
    rows, cols = len(A), len(A[0])
    
    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Perform matrix addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

# Sample matrices
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

B = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Perform addition
result = matrix_addition(A, B)

# Print the result
for row in result:
    print(row)

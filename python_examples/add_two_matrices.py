"""Program to add two matrices."""

def add_two_matrices():
    """Add two matrices and display the result."""
    matrix1 = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]
    matrix2 = [[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]]

    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    print("Matrix 1:")
    for row in matrix1:
        print(row)
    print("\nMatrix 2:")
    for row in matrix2:
        print(row)
    print("\nSum of matrices:")
    for row in result:
        print(row)
    return result

if __name__ == "__main__":
    add_two_matrices()

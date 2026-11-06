"""Program to print a matrix in Z form."""

def print_matrix_in_z_form():
    """Print the elements of a matrix in Z (zigzag) form."""
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    n = len(matrix)

    for j in range(n):
        print(matrix[0][j], end=' ')

    for i in range(1, n - 1):
        print(matrix[i][n - 1 - i], end=' ')

    for j in range(n):
        print(matrix[n - 1][j], end=' ')

    print()
    return True

if __name__ == "__main__":
    print_matrix_in_z_form()

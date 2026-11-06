"""Program to compute the product of two matrices."""

def matrix_product():
    """Multiply two matrices."""
    matrix1 = [[1, 2, 3],
               [4, 5, 6]]
    matrix2 = [[7, 8],
               [9, 10],
               [11, 12]]

    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        print("Matrix multiplication not possible!")
        return None

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    print("Matrix 1:")
    for row in matrix1:
        print(f"  {row}")
    print("\nMatrix 2:")
    for row in matrix2:
        print(f"  {row}")
    print("\nProduct:")
    for row in result:
        print(f"  {row}")
    return result

if __name__ == "__main__":
    matrix_product()

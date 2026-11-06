"""Program to create an n x n matrix."""

def matrix_creation_of_nn():
    """Create an n x n matrix with specific values."""
    n = 3

    matrix1 = [[0] * n for _ in range(n)]

    matrix2 = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(i * n + j + 1)
        matrix2.append(row)

    matrix3 = [[i * n + j + 1 for j in range(n)] for i in range(n)]

    print(f"n = {n}")
    print("Zero matrix:")
    for row in matrix1:
        print(f"  {row}")
    print("\nSequential matrix:")
    for row in matrix2:
        print(f"  {row}")

    return matrix3

if __name__ == "__main__":
    matrix_creation_of_nn()

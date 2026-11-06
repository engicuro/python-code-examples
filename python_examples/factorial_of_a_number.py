"""Program to calculate the factorial of a given number."""

def factorial_of_a_number():
    """Calculate the factorial of a number."""
    num = 5

    result = 1
    for i in range(1, num + 1):
        result *= i

    def factorial_recursive(n):
        if n <= 1:
            return 1
        return n * factorial_recursive(n - 1)

    print(f"Factorial of {num} (iterative): {result}")
    print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
    return result

if __name__ == "__main__":
    factorial_of_a_number()

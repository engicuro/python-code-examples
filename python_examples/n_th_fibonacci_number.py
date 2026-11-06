"""Program to find the N-th Fibonacci number."""

def n_th_fibonacci_number():
    """Find the N-th Fibonacci number."""
    n = 10

    def fib_iterative(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def fib_recursive(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return fib_recursive(n - 1) + fib_recursive(n - 2)

    result_iter = fib_iterative(n)
    result_rec = fib_recursive(n)

    print(f"N = {n}")
    print(f"Fibonacci (iterative): {result_iter}")
    print(f"Fibonacci (recursive): {result_rec}")
    return result_iter

if __name__ == "__main__":
    n_th_fibonacci_number()

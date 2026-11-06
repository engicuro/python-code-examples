"""Program to implement the basic Euclidean algorithm for GCD."""

def basic_euclidean_algorithms():
    """Find GCD of two numbers using the Euclidean algorithm."""
    a = 48
    b = 18

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    result = gcd(a, b)
    print(f"GCD of {a} and {b} is: {result}")
    return result

if __name__ == "__main__":
    basic_euclidean_algorithms()

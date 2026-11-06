"""Program to implement the extended Euclidean algorithm."""

def extended_euclidean_algorithms():
    """Find GCD and coefficients using the extended Euclidean algorithm."""
    a = 48
    b = 18

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = extended_gcd(a, b)
    print(f"Numbers: {a}, {b}")
    print(f"GCD: {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")
    return gcd, x, y

if __name__ == "__main__":
    extended_euclidean_algorithms()

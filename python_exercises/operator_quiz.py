"""Operator - Exercise (Quiz)."""

def operator():
    """Quiz: Demonstrate different Python operators."""
    a = 10
    b = 3

    print(f"a = {a}, b = {b}")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")
    print(f"Floor Division: {a // b}")
    print(f"Modulus: {a % b}")
    print(f"Exponentiation: {a ** b}")

    # Bitwise operators
    print(f"Bitwise AND: {a & b}")
    print(f"Bitwise OR: {a | b}")
    print(f"Bitwise XOR: {a ^ b}")
    print(f"Bitwise NOT: ~{a}")
    print(f"Left shift: {a << 1}")
    print(f"Right shift: {a >> 1}")

if __name__ == "__main__":
    operator()

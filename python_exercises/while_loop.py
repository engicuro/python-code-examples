"""While Loop - Exercise."""

def while_loop():
    """Demonstrate while loop usage."""
    # Print numbers from 1 to 10
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()

    # Print factorial of a number
    num = 5
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    print(f"Factorial: {factorial}")

if __name__ == "__main__":
    while_loop()

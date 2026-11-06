"""Program to calculate simple interest given principal, rate, and time."""

def find_simple_interest():
    """Calculate simple interest."""
    principal = 1000
    rate = 5
    time = 3

    simple_interest = (principal * rate * time) / 100

    print(f"Principal: ${principal}")
    print(f"Rate: {rate}%")
    print(f"Time: {time} years")
    print(f"Simple Interest: ${simple_interest:.2f}")
    return simple_interest

if __name__ == "__main__":
    find_simple_interest()

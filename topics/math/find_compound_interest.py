"""Program to calculate compound interest given principal, rate, and time."""

def find_compound_interest():
    """Calculate compound interest."""
    principal = 10000
    rate = 5
    time = 3
    n = 1

    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    compound_interest = amount - principal

    print(f"Principal: ${principal}")
    print(f"Rate: {rate}%")
    print(f"Time: {time} years")
    print(f"Compound Interest: ${compound_interest:.2f}")
    print(f"Total Amount: ${amount:.2f}")
    return compound_interest

if __name__ == "__main__":
    find_compound_interest()

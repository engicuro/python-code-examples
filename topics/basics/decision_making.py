"""Decision Making - Exercise."""

def decision_making():
    """Demonstrate decision making with if-elif-else."""
    age = 20

    if age < 13:
        print("Child")
    elif age < 18:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Senior")

    # Check if a number is positive, negative, or zero
    num = -5
    if num > 0:
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is zero")

if __name__ == "__main__":
    decision_making()

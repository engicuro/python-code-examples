"""Program to check whether a number is an Armstrong number or not."""

def check_armstrong_number():
    """Check if a number is an Armstrong number."""
    num = 153
    temp = num
    order = len(str(num))
    sum_digits = sum(int(digit) ** order for digit in str(temp))

    print(f"Number: {num}")
    print(f"Number of digits: {order}")
    print(f"Sum of digits raised to power {order}: {sum_digits}")

    if sum_digits == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is NOT an Armstrong number.")

    return sum_digits == num

if __name__ == "__main__":
    check_armstrong_number()

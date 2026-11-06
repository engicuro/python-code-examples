"""Program to find the difference between the sum of odd and even digits of a number."""

def difference_between_sums_of_odd_and_even_digits():
    """Calculate the difference between sum of odd digits and sum of even digits."""
    num = 12345

    digits = [int(d) for d in str(num)]
    odd_sum = sum(d for d in digits if d % 2 != 0)
    even_sum = sum(d for d in digits if d % 2 == 0)
    difference = odd_sum - even_sum

    print(f"Number: {num}")
    print(f"Digits: {digits}")
    print(f"Sum of odd digits: {odd_sum}")
    print(f"Sum of even digits: {even_sum}")
    print(f"Difference (odd - even): {difference}")
    return difference

if __name__ == "__main__":
    difference_between_sums_of_odd_and_even_digits()

"""Program to check if all digits of a number divide the number itself."""

def check_if_all_digits_of_a_number_divide_it():
    """Check if all digits of a number divide the number evenly."""
    num = 128

    def check_divisible(n):
        temp = n
        while temp > 0:
            digit = temp % 10
            if digit == 0 or n % digit != 0:
                return False
            temp //= 10
        return True

    result = check_divisible(num)
    print(f"Number: {num}")
    print(f"All digits divide the number: {result}")
    return result

if __name__ == "__main__":
    check_if_all_digits_of_a_number_divide_it()

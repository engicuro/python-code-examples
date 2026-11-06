"""Program to check whether a given number is prime or not."""

def check_whether_a_number_is_prime_or_not():
    """Check if a number is prime."""
    test_nums = [2, 3, 4, 17, 20, 97, 100]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    for num in test_nums:
        result = is_prime(num)
        print(f"{num} is prime: {result}")

if __name__ == "__main__":
    check_whether_a_number_is_prime_or_not()

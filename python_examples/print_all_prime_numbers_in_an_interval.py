"""Program to print all prime numbers in a given interval."""

def print_all_prime_numbers_in_an_interval():
    """Print all prime numbers within a given range."""
    start = 10
    end = 50

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

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print(f"Prime numbers from {start} to {end}: {primes}")
    return primes

if __name__ == "__main__":
    print_all_prime_numbers_in_an_interval()

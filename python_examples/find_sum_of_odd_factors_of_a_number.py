"""Program to find the sum of odd factors of a number."""

def find_sum_of_odd_factors_of_a_number():
    """Calculate the sum of all odd factors of a given number."""
    num = 15

    def sum_odd_factors(n):
        total = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if i % 2 != 0:
                    total += i
                if i != n // i and (n // i) % 2 != 0:
                    total += n // i
            i += 1
        return total

    result = sum_odd_factors(num)
    print(f"Number: {num}")
    print(f"Sum of odd factors: {result}")
    return result

if __name__ == "__main__":
    find_sum_of_odd_factors_of_a_number()

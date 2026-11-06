"""Program to find the minimum sum of factors of a number."""

def find_minimum_sum_of_factors_of_number():
    """Find the minimum sum of factors of a given number."""
    num = 12

    def min_sum_factors(n):
        factor_sum = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                factor_sum += i
                n //= i
            i += 1
        if n > 1:
            factor_sum += n
        return factor_sum

    result = min_sum_factors(num)
    print(f"Number: {num}")
    print(f"Minimum sum of factors: {result}")
    return result

if __name__ == "__main__":
    find_minimum_sum_of_factors_of_number()

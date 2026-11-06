"""Program to find the product of unique prime factors of a number."""

def product_of_unique_prime_factors_of_a_number():
    """Calculate the product of unique prime factors of a given number."""
    num = 315

    def unique_prime_factors_product(n):
        product = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                product *= i
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            product *= n
        return product

    result = unique_prime_factors_product(num)
    print(f"Number: {num}")
    print(f"Product of unique prime factors: {result}")
    return result

if __name__ == "__main__":
    product_of_unique_prime_factors_of_a_number()

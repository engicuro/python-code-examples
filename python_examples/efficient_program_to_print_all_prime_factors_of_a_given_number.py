"""Program to efficiently print all prime factors of a given number."""

def efficient_program_to_print_all_prime_factors_of_a_given_number():
    """Find all prime factors of a given number efficiently."""
    num = 315

    def prime_factors(n):
        factors = []
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 2:
            factors.append(n)
        return factors

    result = prime_factors(num)
    print(f"Number: {num}")
    print(f"Prime factors: {result}")
    return result

if __name__ == "__main__":
    efficient_program_to_print_all_prime_factors_of_a_given_number()

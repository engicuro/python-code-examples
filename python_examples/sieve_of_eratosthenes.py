"""Program to implement the Sieve of Eratosthenes to find prime numbers."""

def sieve_of_eratosthenes():
    """Find all prime numbers up to a given limit using the Sieve of Eratosthenes."""
    limit = 50

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, limit + 1) if sieve[i]]
    print(f"Prime numbers up to {limit}: {primes}")
    return primes

if __name__ == "__main__":
    sieve_of_eratosthenes()

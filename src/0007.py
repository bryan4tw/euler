# 10001st prime

import timeit
from math import log


# Bruteforce method to find the nth prime number by checking each number for primality.
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def nth_prime_brute(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num


print("Bruteforce method: 10,001st prime number is:", nth_prime_brute(10001))


def prime_sieve(n):
    """Return a list of prime numbers up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def nth_prime(n):
    """Return the nth prime number."""
    if n < 1:
        return None
    # Estimate upper bound for nth prime using n * log(n)
    upper_bound = int(n * (log(n) + log(log(n)))) if n > 5 else 15
    primes = prime_sieve(upper_bound)
    while len(primes) < n:
        upper_bound *= 2  # Double the upper bound if not enough primes found
        primes = prime_sieve(upper_bound)
    return primes[n - 1]


# Print the 10,001st prime number
print("Sieve method: 10,001st prime number is:", nth_prime(10001))

# Benchmark the nth_prime function
execution_time1 = timeit.timeit("nth_prime(10001)", globals=globals(), number=100)
print(f"Average execution time over 100 runs: {execution_time1 / 100:.8f} seconds")
execution_time2 = timeit.timeit("nth_prime_brute(10001)", globals=globals(), number=100)
print(f"Average execution time over 100 runs: {execution_time2 / 100:.8f} seconds")

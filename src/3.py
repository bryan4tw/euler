# Largest prime factor of the number 600851475143?

import timeit


# Function to find the largest prime factor of a number
def largest_prime_factor(n):
    # Start with the smallest prime factor
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n


# Prime sieve function to generate prime numbers up to a limit
def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if is_prime[p]]


# Function to find the largest prime factor using the prime sieve
def largest_prime_factor_with_sieve(n):
    limit = int(n**0.5) + 1
    primes = prime_sieve(limit)
    largest_factor = 1

    for prime in primes:
        while n % prime == 0:
            largest_factor = prime
            n //= prime
        if n == 1:
            break

    if n > 1:  # If n is still greater than 1, it is a prime factor
        largest_factor = n

    return largest_factor


# Print
print("Largest prime factor of 600851475143 is:", largest_prime_factor(600851475143))
print(
    "Largest prime factor of 600851475143 using sieve is:",
    largest_prime_factor_with_sieve(600851475143),
)

# Benchmark the largest_prime_factor function
execution_time1 = timeit.timeit(
    "largest_prime_factor(600851475143)", globals=globals(), number=100
)
print(f"Average execution time over 100 runs: {execution_time1 / 100:.8f} seconds")
execution_time2 = timeit.timeit(
    "largest_prime_factor_with_sieve(600851475143)", globals=globals(), number=100
)
print(f"Average execution time over 100 runs: {execution_time2 / 100:.8f} seconds")

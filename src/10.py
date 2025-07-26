# sum of primes

import timeit


# Prime sieve to find all prime numbers up to n
def prime_sieve_to_n(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


# Sum of all primes up to n
def sum_of_primes(n):
    primes = prime_sieve_to_n(n)
    return sum(primes)


print("Sum of all primes up to 2000000:", sum_of_primes(2000000))

# Timing the execution
execution_time = timeit.timeit(lambda: sum_of_primes(2000000), number=1)
print(f"Execution time: {execution_time:.8f} seconds")

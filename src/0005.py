# Smallest Multiple
import timeit


# Prime sieve to find all prime numbers up to n
def prime_sieve_to_n(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p] == True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


# Find the smallest multiple of all numbers from 1 to n using prime factors
def smallest_multiple(n):
    primes = prime_sieve_to_n(n)
    factors = {}

    for prime in primes:
        max_power = 0
        power = 1
        while prime**power <= n:
            max_power = power
            power += 1
        factors[prime] = max_power

    product = 1
    for prime, power in factors.items():
        product *= prime**power

    return product


# Print the smallest multiple of all numbers from 1 to 20
print("Smallest multiple of all numbers from 1 to 20:", smallest_multiple(20))

# Benchmark the smallest_multiple function
execution_time = timeit.timeit("smallest_multiple(20)", globals=globals(), number=10000)
print(f"Average execution time over 10,000 runs: {execution_time / 10000:.8f} seconds")

# Miread the instructions, none of this is helpful.
# # Identify all prime factors of a number
# def prime_factors(n):
#     factors = []
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             factors.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         factors.append(n)
#     return factors


# # Deduplicate an array
# def deduplicate(arr):
#     return list(set(arr))


# # Append prime factors to a list
# def append_prime_factors_to_list(newfactors, factors):
#     factors.extend(newfactors)


# # Multiply all factors together
# def multiply_factors(factors):
#     product = 1
#     for factor in factors:
#         product *= factor
#     return product


# # Find the smallest multiple of all numbers from 1 to n
# def smallest_multiple(n):
#     factors = []
#     for i in range(2, n + 1):
#         newfactors = prime_factors(i)
#         append_prime_factors_to_list(newfactors, factors)
#     factors = deduplicate(factors)
#     return multiply_factors(factors)


# # Print
# print("Smallest multiple of all numbers from 1 to 20:", smallest_multiple(20))

# # Benchmark the smallest_multiple function
# execution_time = timeit.timeit("smallest_multiple(20)", globals=globals(), number=10000)
# print(f"Average execution time over 10,000 runs: {execution_time / 10000:.8f} seconds")

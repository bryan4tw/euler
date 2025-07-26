# Pythagorean Triplet
import timeit


# multiply array
def multiply_array(arr):
    product = 1
    for num in arr:
        product *= num
    return product


# Brute force solution to find a Pythagorean triplet (a, b, c) such that a + b + c = n
def pythagorean_triplet_brute(n):
    for a in range(1, n):
        for b in range(a + 1, n):
            c = n - a - b
            if c > 0 and a * a + b * b == c * c:
                return a, b, c
    return None


print(multiply_array(pythagorean_triplet_brute(1000)))


# slightly optimized solution by reducing the range of a and b
def pythagorean_triplet_optimized(n):
    for a in range(1, n // 3):
        for b in range(a + 1, n // 2):
            c = n - a - b
            if a * a + b * b == c * c:
                return a, b, c
    return None


print(multiply_array(pythagorean_triplet_optimized(1000)))


# benchmarking
execution_time_brute = timeit.timeit(lambda: pythagorean_triplet_brute(1000), number=10)
print(f"Brute force execution time: {execution_time_brute:.8f} seconds")
execution_time_optimized = timeit.timeit(
    lambda: pythagorean_triplet_optimized(1000), number=10
)
print(f"Optimized execution time: {execution_time_optimized:.8f} seconds")

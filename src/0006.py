# Sum Square Difference

import timeit


def sum_square(n):
    return sum(i**2 for i in range(1, n + 1))


def square_sum(n):
    return sum(range(1, n + 1)) ** 2


def sum_square_difference(n):
    return square_sum(n) - sum_square(n)


# Print the sum square difference for the first 100 natural numbers
print(
    "Sum square difference for the first 100 natural numbers:",
    sum_square_difference(100),
)

# Benchmark the sum_square_difference function
execution_time = timeit.timeit(
    "sum_square_difference(100)", globals=globals(), number=10000
)
print(f"Average execution time over 10,000 runs: {execution_time / 10000:.8f} seconds")

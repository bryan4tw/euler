# Sum of even Fibonacci numbers below 4 million

import timeit


# Generate Fibonacci numbers until the next number exceeds limit, return an array.
def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1
    while a < limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# Loop through the Fibonacci numbers and sum the even ones.
def sum_of_even_fibonacci(fib_sequence):
    total = 0
    for num in fib_sequence:
        if num % 2 == 0:
            total += num
    return total


# Instead of generating all Fibonacci numbers, I will generate them on the fly and sum the even ones.
def sum_of_even_fibonacci_on_the_fly(limit):
    total = 0
    a, b = 0, 1
    while a < limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total


# Print the results of both methods

print(
    sum_of_even_fibonacci(generate_fibonacci(4000000))
)  # Should print the sum of even Fibonacci numbers below 4 million
print(sum_of_even_fibonacci_on_the_fly(4000000))

# Benchmark the two functions
execution_time1 = timeit.timeit(
    "sum_of_even_fibonacci(generate_fibonacci(4000000))",
    globals=globals(),
    number=10000,
)
execution_time2 = timeit.timeit(
    "sum_of_even_fibonacci_on_the_fly(4000000)", globals=globals(), number=10000
)
print(
    f"Average execution time of sum_of_even_fibonacci over 10,000 runs: {execution_time1 / 10000:.8f} seconds"
)
print(
    f"Average execution time of sum_of_even_fibonacci_on_the_fly over 10,000 runs: {execution_time2 / 10000:.8f} seconds"
)

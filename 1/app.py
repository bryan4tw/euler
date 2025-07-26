# Sum of all numbers that are multiples of 3 or 5 below 1000

import timeit


# Iterate through all numbers below 1000 and check if they are multiples of 3 or 5.
# If they are, add them to the total.
# This is a brute force method and can be slow for larger limits.
# The time complexity is O(n), where n is the limit (1000 in this case).
def sum_of_multiples1(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


# Instead of iterating through all 1000 numbers, I am going to multiple 3 while the product is less than 1000, then do the same for 5, but SKIP numbers where the multiple is a multiple of 3.
def sum_of_multiples2(limit):
    total = 0
    for i in range(3, limit, 3):
        total += i
    for i in range(5, limit, 5):
        if i % 3 != 0:  # Skip multiples of 3
            total += i
    return total


print(sum_of_multiples1(1000))
print(sum_of_multiples2(1000))  # Should print True

# Benchmark the two functions
execution_time1 = timeit.timeit(
    "sum_of_multiples1(1000)", globals=globals(), number=10000
)
execution_time2 = timeit.timeit(
    "sum_of_multiples2(1000)", globals=globals(), number=10000
)
print(
    f"Average execution time of sum_of_multiples1 over 10,000 runs: {execution_time1 / 10000:.8f} seconds"
)
print(
    f"Average execution time of sum_of_multiples2 over 10,000 runs: {execution_time2 / 10000:.8f} seconds"
)

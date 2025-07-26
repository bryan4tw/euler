# Palindrome Products

import timeit


# Function to check if a number is a palindrome
def is_palindrome(n):
    return str(n) == str(n)[::-1]


# Function to find the largest palindrome product of two 3-digit numbers
def largest_palindrome_product1():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):  # Start j from i to avoid duplicate pairs
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome


# Work backwards and break early if the product is less than the current max
def largest_palindrome_product2():
    max_palindrome = 0
    # Search 999 through 899 and assume there will be a palindrome product
    for i in range(999, 899, -1):
        for j in range(i, 899, -1):  # Start j from i to avoid duplicate pairs
            product = i * j
            if (
                product < max_palindrome
            ):  # No need to check further if product is less than current max
                break
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome


print(
    "Largest palindrome product of two 3-digit numbers (method 1):",
    largest_palindrome_product1(),
)

print(
    "Largest palindrome product of two 3-digit numbers (method 2):",
    largest_palindrome_product2(),
)

# Benchmark
execution_time1 = timeit.timeit(
    "largest_palindrome_product1()", globals=globals(), number=100
)
print(f"Execution time (method 1): {execution_time1 / 100:.8f} seconds")
execution_time2 = timeit.timeit(
    "largest_palindrome_product2()", globals=globals(), number=100
)
print(f"Execution time (method 2): {execution_time2 / 100:.8f} seconds")

# Factorial Digit Sum

from math import factorial
import timeit


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


print(f"Sum of digits in 100!: {sum_of_digits(factorial(100))}")


# Factorial the fun way
def factorial4fun(n):
    if n == 0:
        return 1
    else:
        return n * factorial4fun(n - 1)


# Factorial without recursion
def factorial4fun_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(f"recursive: {sum_of_digits(factorial4fun(100))}")
print(f"iterative: {sum_of_digits(factorial4fun_iterative(100))}")

execution_time1 = timeit.timeit(lambda: sum_of_digits(factorial(100)), number=10000)
execution_time2 = timeit.timeit(lambda: sum_of_digits(factorial4fun(100)), number=10000)
execution_time3 = timeit.timeit(
    lambda: sum_of_digits(factorial4fun_iterative(100)), number=10000
)

print(f"factorial: {execution_time1/10000:.6f} seconds")
print(f"recursive: {execution_time2/10000:.6f} seconds")
print(f"iterative: {execution_time3/10000:.6f} seconds")

# surprisingly, the iterative version is faster than the recursive version

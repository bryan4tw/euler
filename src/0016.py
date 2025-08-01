# Power Digit Sum

import timeit
import math

bignumber = 2**1000


def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


print(f"Sum of digits is {sum_of_digits(bignumber)}")

execution_time = timeit.timeit(
    "sum_of_digits(bignumber)", globals=globals(), number=10000
)
print(f"Execution time: {execution_time:.8f} seconds")

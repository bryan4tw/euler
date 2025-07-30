# Highly Divisible Triangular Number

import timeit


def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2  # i and n // i
            if i * i == n:  # Perfect square
                count -= 1
    return count


def triangle_number(n):
    return n * (n + 1) // 2


def highly_divisible_triangular_number():
    n = 10000  # start a bit higher to find a number with more divisors
    while True:
        tri_num = triangle_number(n)
        if count_divisors(tri_num) > 500:
            return tri_num
        n += 1


print(
    "First triangular number with over 500 divisors:",
    highly_divisible_triangular_number(),
)

execution_time = timeit.timeit(
    "highly_divisible_triangular_number()", globals=globals(), number=10
)
print(f"Average execution time over 10 runs: {execution_time / 10:.8f} seconds")

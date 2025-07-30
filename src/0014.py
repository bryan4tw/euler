# Longest Collatz Sequence

import timeit


def odd_collatz(n):
    return 3 * n + 1


def even_collatz(n):
    return n // 2


# return the length of the Collatz sequence starting from n
def collatz_sequence_length(n):
    max_length = 0
    while n != 1:
        if n % 2 == 0:
            n = even_collatz(n)
        else:
            n = odd_collatz(n)
        max_length += 1
    return max_length


def longest_collatz_sequence(limit):
    max_length = 0
    number = 0
    for i in range(1, limit):
        # print no new line
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            number = i
    return number


print(
    f"Longest collatz sequence under 1,000,000 starts with: {longest_collatz_sequence(1000000)}"
)

execution_time = timeit.timeit(
    "longest_collatz_sequence(1000000)", globals=globals(), number=10
)
print(f"Average execution time over 10 runs: {execution_time / 10:.8f} seconds")

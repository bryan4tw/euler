# Amicable Numbers


def d(n):
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


def amicable_numbers(limit):
    amicable_pairs = []
    for a in range(2, limit):
        b = d(a)
        if b > a and d(b) == a:
            amicable_pairs.append((a, b))
    return amicable_pairs


print(
    f"sum of amicable numbers under 10000: {sum(a + b for a, b in amicable_numbers(10000))}"
)

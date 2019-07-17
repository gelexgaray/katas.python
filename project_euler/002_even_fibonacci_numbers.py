# https://projecteuler.net/problem=2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def even_fibonacci_sum(range_end: int):
    total: int = 0
    last: int = 1
    previous: int = 0
    current = last + previous
    while current <= range_end:
        if (current % 2) != 0:
            total += current
        previous = last
        last = current
        current = last + previous
    return total


print("sum till 89 should be: ", (1 + 3 + 5 + 13 + 21 + 55 + 89))
print()
print("First approach")
print("even_fibonacci_sum(89)", even_fibonacci_sum(89))
print("even_fibonacci_sum(4000000)", even_fibonacci_sum(4000000))
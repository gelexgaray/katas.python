# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# Based on Stack Overflow thread
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors#22808285
def largest_prime_factor(number: int):
    factor = 2
    while factor * factor <= number:  # until factor^2 > number
        if number % factor == 0:
            number = number // factor
        else:
            factor += 1
    return number


print(largest_prime_factor(600851475143))  # 6857


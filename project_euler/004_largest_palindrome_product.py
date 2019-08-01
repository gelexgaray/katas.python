# https://projecteuler.net/problem=4
# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome_number(number: int):
    number_string = str(number)
    return number_string == number_string[::-1]


def find_largest_palindrome(range_min: int, range_max: int):
    for number1 in range(range_max, range_min, -1):
        for number2 in range(range_max, range_min, -1):
            product = number1 * number2
            if is_palindrome_number(product):
                print("%s * %s = %s" % (number1, number2, product))
                return
    return


print("two digit:")
find_largest_palindrome(10, 99)

print("three digit:")
find_largest_palindrome(100, 999)

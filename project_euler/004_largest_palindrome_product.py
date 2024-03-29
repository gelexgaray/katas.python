# https://projecteuler.net/problem=4
# Largest palindrome product
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome_number(number: int):
    number_string = str(number)
    return number_string == number_string[::-1]


def find_largest_palindrome(range_min: int, range_max: int):
    largest_result = 0
    largest_op1 = 0
    largest_op2 = 0
    for current_op1 in range(range_max, range_min, -1):
        for current_op2 in range(range_max, range_min, -1):
            test_result = current_op1 * current_op2
            if is_palindrome_number(test_result):
                if test_result > largest_result:
                    largest_result = test_result
                    largest_op1 = current_op1
                    largest_op2 = current_op2
                else:
                    break
    print("%s * %s = %s" % (largest_op1, largest_op2, largest_result))
    return


print("two digit:")
find_largest_palindrome(10, 99)

print("three digit:")
find_largest_palindrome(100, 999)

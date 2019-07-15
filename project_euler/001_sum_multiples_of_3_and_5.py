# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
def sum_multiples_of_3_and_5(to_number: int ):
    sum_of_values:int = 0
    for number in range(3, to_number) :
        if number % 3 == 0 or number % 5 == 0:
            sum_of_values += number
    return sum_of_values

# Less iterations
def sum_multiples_of_3_and_5_opt1(to_number: int ):
    sum_of_values: int = sum(range(3, to_number, 3))
    for number in range(5, to_number, 5) :
        if number % 3 != 0:
            sum_of_values += number
    return sum_of_values

# Python sum version
def sum_multiples_of_3_and_5_opt2(to_number: int ):
    return sum(range(3, to_number, 3)) \
           + sum(range(5, to_number, 5)) \
           - sum(range(15, to_number, 15))

# Gaussian sum version: Kudos for Ramon!!
def sum_multiples_of_3_and_5_gauss(to_number: int ):
    return sum_multiples_of_gauss(3, to_number - 1) \
           + sum_multiples_of_gauss(5, to_number - 1) \
           - sum_multiples_of_gauss(15, to_number - 1)

def sum_multiples_of_gauss(base_number: int, limit_number: int):
    number = limit_number // base_number
    return  base_number * (number + 1) * number / 2


# Test executions
print("Loop version")
print(sum_multiples_of_3_and_5(10) ) # 23
print(sum_multiples_of_3_and_5(1000) ) # 233168
print()

print("Loop version with less iterations (OPT1)")
print(sum_multiples_of_3_and_5_opt1(10) ) # 23
print(sum_multiples_of_3_and_5_opt1(1000) ) # 233168
print()

print("Loop version with less iterations (OPT2)")
print(sum_multiples_of_3_and_5_opt2(10) ) # 23
print(sum_multiples_of_3_and_5_opt2(1000) ) # 233168
print()

print("Gauss sum version (non iterative)")
print(sum_multiples_of_3_and_5_gauss(10) ) # 23 ?
print(sum_multiples_of_3_and_5_gauss(1000) ) # 233168 ?
print()

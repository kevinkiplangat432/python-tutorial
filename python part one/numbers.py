# Use abs(), pow(), max(), and min() on a set of numbers.
import math
import random  
numbers = [-10, 5, 3.5, -2.8, 0]
print("Absolute values:", [abs(num) for num in numbers])
print("Power of 2 raised to 3:", pow(2, 3))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

#abs
# For integers
print(abs(-5))  # Output: 5
print(abs(10))  # Output: 10
print(abs(0))   # Output: 0

# For floating-point numbers
print(abs(-3.14)) # Output: 3.14
print(abs(2.71))  # Output: 2.71

# For complex numbers
print(abs(3 + 4j)) # Output: 5.0 (calculated as sqrt(3^2 + 4^2))
print(abs(-2 - 5j)) # Output: 5.385164807134504 (calculated as sqrt((-2)^2 + (-5)^2))


#pow
result = pow(2, 3)  # result will be 8 (2 * 2 * 2)
result = pow(10, 2, 9)  # result will be 1 (10**2 = 100, 100 % 9 = 1)

#max and min
values = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maximum = max(values)  # maximum will be 9
minimum = min(values)  # minimum will be 1  
print("Max:", maximum)
print("Min:", minimum)


# Round a float to 2 decimal places.
float_number = 3.14159
rounded_number = round(float_number, 2)
print(rounded_number)

# Use floor division // and modulo % in one expression to print quotient and remainder.
dividend = 17
divisor = 4
quotient = dividend // divisor
remainder = dividend % divisor
print("Quotient:", quotient)
print("Remainder:", remainder)

# Generate a random integer between 1 and 100 using random.
random_integer = random.randint(1, 100)
print(random_integer)


# Show the difference between integer division and float division.
int_division = 7 // 3  # Integer division
float_division = 7 / 3  # Float division
print("Integer Division:", int_division)
print("Float Division:", float_division)

# Create a small math expression mixing **, //, and %.
expression_result = (5 ** 2) // 3 % 4
print("Expression Result:", expression_result)


# Compare the results of 3 ** 2 ** 2 and (3 ** 2) ** 2.
result1 = 3 ** 2 ** 2  # This is evaluated as 3 ** (2 ** 2) = 3 ** 4 = 81
result2 = (3 ** 2) ** 2  # This is evaluated as (3 ** 2) ** 2 = 9 ** 2 = 81
print("3 ** 2 ** 2 =", result1)
print("(3 ** 2) ** 2 =", result2)   
# Both results are equal to 81
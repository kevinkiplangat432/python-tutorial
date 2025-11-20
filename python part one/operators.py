# Demonstrate arithmetic, assignment, comparison, and logical operators in one snippet.
# Perform basic arithmetic operations on two numbers.
x = 15
y = 4
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y)  # Modulus
print(x ** y) # Exponentiation
# Use assignment operators to modify a variable.
z = 10
z += 5  # Equivalent to z = z + 5
print(z)
z *= 2  # Equivalent to z = z * 2
print(z)
# Compare two variables using comparison operators.
a = 20
b = 15
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
print(a == b)  # Equal to
print(a != b)  # Not equal to
# Combine boolean values using logical operators.
bool1 = True    

# Use bitwise AND and OR on two integers.
bool2 = False
print(bool1 and bool2)  # Logical AND
print(bool1 or bool2)   # Logical OR


# Show the difference between is and == using two lists.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True, because values are the same
print(list1 is list2)  # False, because they are different objects in memory


# Use a compound assignment operator to update a variable.
count = 0
count += 1  # Increment count by 1
print(count)
count *= 3  # Multiply count by 3
print(count)

# Write an expression mixing arithmetic and comparison in a single line.
result = (x + y) > (a - b)
print(result)

# Show the operator precedence using parentheses.
value = 5 + 3 * 2  # Without parentheses
print(value)  # Outputs 11

# Predict and test:
value_with_parentheses = (5 + 3) * 2  # With parentheses
print(value_with_parentheses)  # Outputs 16
# Use bitwise operators on two integers.
num1 = 6  # In binary: 110
num2 = 3  # In binary: 011
print(num1 & num2)  # Bitwise AND: 010 (2 in decimal)
print(num1 | num2)  # Bitwise OR: 111 (7 in decimal
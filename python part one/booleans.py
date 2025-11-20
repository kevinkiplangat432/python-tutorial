# Evaluate the truthiness of an empty list, tuple, set, and string.
empty_list = []
empty_tuple = ()
empty_set = set()
empty_string = ""

# Compare two numbers using all relational operators.
a = 5
b = 10
print(a < b)   # Less than
print(a <= b)  # Less than or equal to
print(a > b)   # Greater than
print(a >= b)  # Greater than or equal to
print(a == b)  # Equal to
print(a != b)  # Not equal to


# Write an expression using and, or, and not.
x = True
y = False
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT

# Use a conditional expression (ternary operator) with a boolean condition.
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# Show the output of bool(0) and bool("False").
print(bool(0))         # Output: False
print(bool("False"))   # Output: True

# Check if a variable is None using is.
var = None
print(var is None)  # Output: True

# Create a boolean condition inside a function that returns early if false.
def check_positive(number):
    if not number > 0:
        return "Number is not positive."
    return "Number is positive."
print(check_positive(-3))
print(check_positive(5))

# Lambda Functions Practice

# Task 1: Lambda to multiply two numbers
multiply = lambda a, b: a * b
print("Task 1 - Multiply two numbers (3 * 4):", multiply(3, 4))


# Task 2: Use lambda with map() to square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("Task 2 - Squares:", squared)


# Task 3: Use lambda with filter() to return only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Task 3 - Even numbers:", even_numbers)


# Task 4: Sort a list of tuples by the second element using lambda
pairs = [(2, 5), (1, 2), (4, 4), (2, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Task 4 - Sorted by second element:", sorted_pairs)


# Flask Prep Connection (conceptual note)
# In Flask routes, lambdas are often used for short transformations:
# Example:
# users = [{"name": "Kevin", "age": 21}, {"name": "Alice", "age": 19}]
# adults = list(filter(lambda u: u["age"] >= 18, users))
# This helps you quickly filter or transform data inline without defining full functions.

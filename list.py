# Task:
# Create a list of 10 numbers.
numbers = [5, 12, 7, 3, 9, 14, 6, 2, 11, 8]

# Filter the list to keep only odd numbers.
odd_numbers = [num for num in numbers if num % 2 != 0]

# Square the remaining numbers.
squared_numbers = [num ** 2 for num in odd_numbers]

# Sort the squared numbers in descending order.
squared_numbers.sort(reverse=True)

# Copy the final list and join it with [100, 200].
final_list = squared_numbers.copy()

final_list.extend([100, 200])

# Print the result.
print(final_list)


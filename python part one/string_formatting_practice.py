# String Formatting

# Task 1: Using f-strings
name = "Kevin"
balance = 4500
print(f"Task 1:\nWelcome, {name}! Your balance is {balance} KES.\n")


# Task 2: Using .format() and % formatting
# Using .format()
print("Task 2:")
print("Welcome, {}! Your balance is {} KES.".format(name, balance))

# Using % formatting
print("Welcome, %s! Your balance is %d KES.\n" % (name, balance))


# Task 3: Align and format strings in a table-like structure
print("Task 3:")
print(f"{'Name':<10} {'Balance':>10}")
print("-" * 22)
print(f"{'Kevin':<10} {4500:>10}")
print(f"{'Alice':<10} {12500:>10}")
print(f"{'Brian':<10} {700:>10}")

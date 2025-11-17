# Try and Except Examples

# Task 1: Handle ZeroDivisionError
print("Task 1:")
try:
    num1 = float(input("Enter numerator: "))
    num2 = float(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter numeric values only.")
print()


# Task 2: Handle FileNotFoundError
print("Task 2:")
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("Error: File not found. Please check the file name or path.")
print()


# Task 3: Demonstrate try/except/else/finally flow
print("Task 3:")
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    division = x / y
except ZeroDivisionError:
    print("Caught ZeroDivisionError: Cannot divide by zero.")
except ValueError:
    print("Caught ValueError: Please enter valid integers.")
else:
    # Runs only if no exception occurs
    print(f"Division successful! Result = {division}")
finally:
    # Always runs, no matter what
    print("Execution complete. Cleaning up resources or closing connections.")

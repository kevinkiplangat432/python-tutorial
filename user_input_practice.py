# User Input Tasks

# Task 1: Prompt the user for their name and greet them
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the program.\n")


# Task 2 and 3: Ask for two numbers and display their sum, handling invalid input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.")
except ValueError:
    print("Invalid input! Please enter numeric values only.")



#in flask 
# from flask import request

# @app.route('/add', methods=['POST'])
# def add_numbers():
#     try:
#         num1 = float(request.form['num1'])
#         num2 = float(request.form['num2'])
#         return f"The sum is {num1 + num2}"
#     except ValueError:
#         return "Invalid input!"

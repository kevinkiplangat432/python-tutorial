# Ask for a user's age
age_input = input("Enter your age: ")

# Check if input is numeric
if not age_input.isdigit():
    print("Invalid input! Please enter a number.")
else:
    # Convert input to integer
    age = int(age_input)

    # Check age categories
    if age < 13:
        print("Child")
    elif 13 <= age <= 19:
        print("Teen")
    elif 20 <= age <= 64:
        print("Adult")
    else:
        print("Senior")

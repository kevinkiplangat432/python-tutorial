# Define the function
def analyze_numbers(numbers):
    # Calculate required values
    max_num = max(numbers)
    min_num = min(numbers)
    average = sum(numbers) / len(numbers)
    squares = [num ** 2 for num in numbers]

    # Return a dictionary with all results
    return {
        "max": max_num,
        "min": min_num,
        "average": average,
        "squares": squares
    }

# Example list
nums = [2, 5, 8, 3, 10]

# Call the function
result = analyze_numbers(nums)

# Print results neatly formatted
print("Analysis Results:")
print(f"Maximum: {result['max']}")
print(f"Minimum: {result['min']}")
print(f"Average: {result['average']:.2f}")
print(f"Squares: {result['squares']}")

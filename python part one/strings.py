# Slice a string to reverse it.
reversed_string = "PythonRocks"[::-1]
print(reversed_string)

# Extract every second character from "PythonRocks".
every_second_char = "PythonRocks"[::2]
print(every_second_char)

# Replace a word in a string using .replace().
original_string = "I love programming in Python."
modified_string = original_string.replace("Python", "JavaScript")
print(modified_string)


# Combine three strings with space separators.
str1 = "Hello"
str2 = "world"
str3 = "!"
combined_string = " ".join([str1, str2, str3])
print(combined_string)

# Use an f-string to format a message with variables.
name = "Alice"
age = 30
formatted_message = f"My name is {name} and I am {age} years old."
print(formatted_message)


# Include quotes inside a string using escape sequences.
quote_string = "She said, \"It's a beautiful day!\""
print(quote_string)

# Count how many times a specific letter appears in a sentence (case insensitive).
sentence = "The quick brown fox jumps over the lazy dog."
letter_to_count = 'o'
count = sentence.lower().count(letter_to_count.lower())
print(f"The letter '{letter_to_count}' appears {count} times.")
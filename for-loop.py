# List of names
names = ["Kevin", "Alice", "Mark"]

# Loop over the list
for name in names:
    # Print the name in uppercase
    print(name.upper())

    # Nested loop to print each letter separately
    for letter in name:
        print(letter)
    
    

# Else clause runs after the loop finishes
else:
    print("All names have been printed successfully!")

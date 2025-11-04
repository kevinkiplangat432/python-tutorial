# Initialize countdown start
count = 10

# Start while loop
while count >= 0:
    # Skip number 5
    if count == 5:
        count -= 1
        continue

    # Break if it reaches 2
    if count == 2:
        print("Countdown stopped at 2!")
        break

    print(count)
    count -= 1  # Decrease the counter each time

# Print final message
print("Blast off!")

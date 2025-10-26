# Task:
# Given a tuple (5, 10, 15, 20, 25):
my_tuple = (5, 10, 15, 20, 25)

# Unpack it into 5 variables
a, b, c, d, e = my_tuple

# Create a new tuple with each element multiplied by 2
new_tuple = tuple(x * 2 for x in my_tuple)


# Loop through it and print values greater than 20
for value in new_tuple:
    if value > 20:
        print(value)

# Join it with another tuple (100, 200)
another_tuple = (100, 200)
joined_tuple = my_tuple + another_tuple

# Use a tuple method to count occurrences of 10
count_of_10 = my_tuple.count(10)
print("Count of 10 in my_tuple:", count_of_10)
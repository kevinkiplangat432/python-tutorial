# Convert a float to an integer and explain the output.

#convert a float to an integer
float_num = 7.89
int_num = int(float_num)
print("They are not equal.")
print(int_num)


#convert  a negative float to an integer
positive_float = -3.14
negative_int = int(positive_float)
print(negative_int)

#convert a float representing whole number to an integer    
whole_float = 10.0
whole_int = int(whole_float)
print(whole_int)




# Convert a string "25" to an integer and add 5.
string_number = "123"
integer_number = int(string_number)
print(integer_number)
print(type(integer_number))

# Binary string to integer
binary_string = "1011"
decimal_from_binary = int(binary_string, 2)
print(decimal_from_binary)

# Hexadecimal string to integer
hex_string = "A5"
decimal_from_hex = int(hex_string, 16)
print(decimal_from_hex)

# Convert a number to a string and concatenate it with another string.
num = 50
num_str = str(num)
concatenated_str = num_str + " is the number"
print(concatenated_str)

# Convert a list of string numbers ["1", "2", "3"] to integers using list comprehension.
str_list = ["1", "2", "3"]
int_list = [int(i) for i in str_list]
print(int_list)

# Cast a tuple to a list, modify it, and cast it back.
my_tuple = (10, 20, 30)
temp_list = list(my_tuple)
temp_list.append(40)
modified_tuple = tuple(temp_list)
print(modified_tuple)


# Convert a boolean True to an integer and explain the result.
bool_value = False
int_from_bool = int(bool_value)
print(int_from_bool)

# Predict:
# In Python, the boolean value True is converted to the integer 1, and False is converted to 0.# Therefore, converting False to an integer results in 0.# The float is truncated towards zero when converted to an integer, so 7.89 becomes 7.# Therefore, converting False to an integer results in 0.
# The float is truncated towards zero when converted to an integer, so 7.89 becomes 7.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.
# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.
# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.# Therefore, converting False to an integer results in 0.      
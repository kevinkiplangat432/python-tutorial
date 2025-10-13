# Create variables of each core type (int, float, complex, str, list, tuple, dict, set, bool).
intvar = 20
floatvar= 3.5678
complexvar =5 + 6j
strvar = "kevin loves coding"
myList =[1,2,3,4,5,6,7,8,9]
myTuple = ("banana", "orange", "cherry")
myDict ={}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
my_set = {"apple", "banana", "cherry"}
is_student = True
has_passed = False #bool


# Check the data type of each using type().
print(type(intvar))
print(type(floatvar))
print(type(complexvar))
print(type(strvar))
print(type(myList))
print(type(myTuple))
print(type(myDict))
print(type(person))
print(type(my_set))
print(type(is_student))
print(type(has_passed))


# Create a complex number and print its real and imaginary parts.
z = 3 + 4j
print(z.real)
print(z.imag)

# Convert a list to a tuple and verify the type.
list1 =[1,2,3,4,5]
mytuple =tuple(list1)
print(type(mytuple))



# Create a mixed list and check the type of each element with a loop.
# Creating a mixed list
mixed_list = [42, "hello", 3.14, True, [1, 2, 3]]

for i in mixed_list:
    print(type(i))
# Write code that checks if two different data types can be compared using ==.
# Sample variables
a = 5        # int
b = "5"      # str

# Try to compare
try:
    if a == b:
        print("They are equal.")
    else:
        print("They are not equal.")
except TypeError:
    print("These two data types cannot be compared.")


# Explain what happens when you multiply a string by an integer in Python.
#str and int
s = "Hello"
n = 3

result = s * n
print(result)

#int and str
n = 4
s = "Hi"

print(n * s)


#str and str
"Hello" * "3"
# This will cause an error because you can't multiply a string by a string
"Hello" * "3"  # TypeError: can't multiply sequence by non-int of type 'str'
# correct way
print("Hello" * 3)         # Works
print("Hello" * int("3"))  # Also works if number is a string

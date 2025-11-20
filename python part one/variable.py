# Create three variables x, y, and z and assign them values in one line.
x,y,z = "Orange", "berry", "zoo"

# Use one variable name to store another variable’s value.
name ="kevin"
FirstName = name

# Write a function that modifies a global variable from inside the function.
def myfunc():
    global name
    name ="Alvin"
myfunc()
# Swap two variables without using a third variable.
a= 10
b= 20
a,b = b,a
# Assign multiple strings to multiple variables and print them formatted in one line.
Name,feeling,action = "kevin","loves","coding"
print(Name+feeling+action)

# Explain what happens when you assign a mutable vs immutable value to a variable.


#immutable
#int
#str
#tuple
#on reassigning it creates new object
Num = 10
Age = Num
Age = 20
print(Num)# output = 10
print(Age)# output =20

#dispite assigning a new value to Age which was equal to Num it did not change the value of Num that's immutability




#mutability
Li =[1,2,3,4,5,6]
NewLi= Li
NewLi.append([7,8,9])

print(NewLi) # outputs 1,2,3,4,5,6,7,8,9
print(Li) # outputs 1,2,3,4,5,6,7,8,9

#how to copy a Mutable object.
NewLi = Li.copy()
NewLi.append([7,8,9])

print(NewLi) # outputs 1,2,3,4,5,6,7,8,9
print(Li) # outputs 1,2,3,4,5,6

# Sets
my_set= {1,2,3,"banana","orange","potato"}
print(my_set)

# Task:
# Create two sets: {1,2,3,4,5} and {4,5,6,7}
first_set={1,2,3,4,5}
second_set={4,5,6,7}


# Find union, intersection, and difference
#using the union
union_set =first_set.union(second_set)
print(union_set)
#using the intersection
intersection_set =first_set.intersection(second_set)
print(intersection_set)

#using the difference
difference_set =first_set.difference(second_set)
print(difference_set)

#another way of using difference set 
difference_set2=first_set - second_set
print(difference_set2)
# Add a new element to the first set
my_set.add("cherry")
print(my_set)
#Adding multiple items
new_items=["pineapple","mango","papaya"]
my_set.update(new_items)
print (my_set)
#or
fruits = {"apple", "banana", "cherry"}
tropical_fruits = {"pineapple", "mango", "papaya"}
fruits.update(tropical_fruits)
print(fruits)

# Remove one element safely
#remopve method
remove_set={"orange","pineapple"}

remove_set.remove("orange")
print(remove_set)

#discard method
discard_set={"orange","pineapple"}
discard_set.discard("orange")
print(discard_set)

#pop()
pop_set={"orange","pineapple"}
pop_set.pop()
print(pop_set)

#clear
clear_set = {"apple", "banana", "cherry"}
clear_set.clear()
print(clear_set)  # Output: set()

#del
del_set = {"apple", "banana", "cherry"}
del del_set
#print(del_set) # This would raise a NameError 

#set difference
difference_set={2, 3, 4, 5}
elements_to_remove = {3, 5}
new_set = difference_set - elements_to_remove
print(new_set)  # Output: {1, 2, 4}

# Loop through and print all unique values
fruits1 = {"apple", "banana", "mango", "orange"}

for fruit in fruits1:
    print(fruit)


# Clear the second set and check emptiness
# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Before clearing:")
print("Set1:", set1)
print("Set2:", set2)

# Clear the second set
set2.clear()

# Check if the second set is empty
if len(set2) == 0:
    print("\nSet2 is now empty!")
else:
    print("\nSet2 still has items!")

# Another way to check (more Pythonic)
if not set2:
    print("Confirmed again — Set2 is empty.")

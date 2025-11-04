# Create a dictionary representing a student with keys: name, age, grades (list).
student = {
    "name": "kevin",
    "age": 21,
    "grades": [65, 86, 90]
}

print("Original student dictionary:")
print(student)

# Access the name and add a new key 'average'.
print("\nStudent name:", student["name"])

# Calculate and add average grade
average_grade = sum(student["grades"]) / len(student["grades"])
student["average"] = average_grade

print("\nAfter adding average:")
print(student)

# Remove one key and use .get() to handle missing values.
removed_age = student.pop("age", None)
print("\nRemoved 'age' key:", removed_age)

# Using .get() to safely access a missing key
print("Trying to access 'age' after removal:", student.get("age", "Key not found"))

# Loop through keys and values.
print("\nLooping through student dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Copy it to another variable and update age.
student_copy = student.copy()
student_copy["age"] = 22

print("\nCopied and updated student dictionary:")
print(student_copy)

# Create a nested dictionary of two students and print their average grades.
students = {
    "student1": student,
    "student2": {
        "name": "Alice",
        "age": 20,
        "grades": [78, 85, 92]
    }
}

# Add averages for both
for s in students.values():
    s["average"] = sum(s["grades"]) / len(s["grades"])

print("\nNested students dictionary:")
print(students)

print("\nAverage grades:")
for name, info in students.items():
    print(f"{info['name']}'s average grade: {info['average']}")

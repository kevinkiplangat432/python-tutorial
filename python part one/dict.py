students_details = {
    "student1": {
        "name": "kevin",
        "age": 21,
        "grades": [65, 86, 90]
    },
    "student2": {
        "name": "Alice",
        "age": 20,
        "grades": [78, 85, 92]
    }
}

name = students_details.get("student1",{}) .get("name")
print (students_details["student1"]["name"])

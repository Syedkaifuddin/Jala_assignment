# 1. Create a dictionary with 5 key-value pairs (Student ID: Name)
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "Diana",
    105: "Ethan"
}
print("Initial dictionary:", students)

# 1.1 Adding values in dictionary
students[106] = "Fiona"
print("\nAfter adding (106: Fiona):", students)

# 1.2 Updating values in dictionary
students[102] = "Bobby"
print("\nAfter updating ID 102 to 'Bobby':", students)

# 1.3 Accessing value in dictionary
print("\nAccessing student with ID 103:", students[103])

# 1.4 Create a nested dictionary (e.g., student ID mapped to a dict of info)
nested_students = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bobby", "age": 21, "grade": "B"},
    103: {"name": "Charlie", "age": 19, "grade": "A"},
}
print("\nNested dictionary:", nested_students)

# 1.5 Access values of nested dictionary
print("\nAccess name of student 101:", nested_students[101]["name"])
print("Access grade of student 103:", nested_students[103]["grade"])

# 1.6 Print keys present in dictionary
print("\nKeys in students dictionary:", list(students.keys()))
print("Keys in nested_students dictionary:", list(nested_students.keys()))

# 1.7 Delete a value from dictionary (delete student ID 105)
del students[105]
print("\nAfter deleting student with ID 105:", students)

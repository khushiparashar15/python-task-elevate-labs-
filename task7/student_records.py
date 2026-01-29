import json

# 1. Dictionary with student details
students = {
    "101": {"name": "Aman", "age": 20, "course": "Python"},
    "102": {"name": "Riya", "age": 21, "course": "Java"},
    "103": {"name": "Khushi", "age": 19, "course": "Data Science"}
}

# 2. Access keys and values
print("Student IDs:", students.keys())
print("Student Data:", students.values())

# 3. Update entry
students["102"]["course"] = "Web Development"

# 4. Delete entry
del students["101"]

# 5. Loop through dictionary
print("\n--- Student Records ---")
for sid, info in students.items():
    print(sid, "->", info)

# 6. Convert dictionary to JSON
json_data = json.dumps(students, indent=4)

# 7. Save JSON to file
with open("students.json", "w") as file:
    file.write(json_data)

# 8. Read JSON back into Python
with open("students.json", "r") as file:
    data = json.load(file)

# 9. Print formatted output
print("\n--- Data from JSON File ---")
for sid, info in data.items():
    print(f"ID: {sid}")
    print(f" Name: {info['name']}")
    print(f" Age: {info['age']}")
    print(f" Course: {info['course']}\n")

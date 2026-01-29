# 1. List of students
students = ["Aman", "Riya", "Khushi", "Aman"]

print("Original List:", students)

# 2. Add and remove
students.append("Neha")
students.remove("Aman")   # removes first Aman
print("After add/remove:", students)

# 3. Sort list
students.sort()
print("Sorted List:", students)

# 4. Tuple (fixed data)
fixed_data = ("Python", 2026)
print("\nTuple:", fixed_data)

# 5. Convert list to set (remove duplicates)
student_set = set(students)
print("\nSet (no duplicates):", student_set)

# 6. Set operations
other_set = {"Riya", "Neha", "Karan"}

print("Union:", student_set | other_set)
print("Intersection:", student_set & other_set)
print("Difference:", student_set - other_set)

# 7. Iterate over collections
print("\nIterating List:")
for s in students:
    print(s)

print("\nIterating Set:")
for s in student_set:
    print(s)

# 8. Mutable vs Immutable
students[0] = "Changed"
print("\nList after change:", students)







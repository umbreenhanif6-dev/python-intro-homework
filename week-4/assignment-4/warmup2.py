"""""
Warmup 2: Dictionary Operations
Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects
 (a list of subject strings). Then:
1.Print each key-value pair using .items() in a for loop
2.Add a new key "graduated" with the value False
3.Print the updated dictionary

"""""

student = {
    "Name": "Aiden",
    "Grade": 12,
    "Subjects": ["Literature", "Mathematics", "Earth Science"]
}

for key, value in student.items():
    if isinstance(value, list):
        value = ", ".join(value)
    print(f"{key}: {value}")

print("\nUpdated Student Entry:\n")  # Heading between the outputs

student["Graduated"] = False

for key, value in student.items():
    if isinstance(value, list):
        value = ", ".join(value)
    print(f"{key}: {value}")
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
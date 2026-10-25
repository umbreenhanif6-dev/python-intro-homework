"""
Warmup 2: Dictionary Operations
Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
1.Print each key-value pair using .items() in a for loop
2.Add a new key "graduated" with the value False
3.Print the updated dictionary

"""
student = { "name" :  "Aiden", "grade":  12,  "subject" : ["literature"] }
for key, value in student.items():
	print(f"{key}: {value}")

student["graduated"] = False
print(student)
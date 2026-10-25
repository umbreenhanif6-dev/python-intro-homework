student = { "name" :  "Aiden", "grade":  12,  "subject" : ["literature"] }
for key, value in student.items():
	print(f"{key}: {value}")

student["graduated"] = False
print(student)
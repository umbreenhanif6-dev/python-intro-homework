# List of student dictionaries

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
] # <-- 

# student -> {"name": "Jazmine", "score": 88, "subject": "Python"}

# Create The best student dict to represent the current best student
current_best_student = {"name": "Jazmine", "score": 88}
for student in students:
  # compare currently top score with current student score
  if student["score"] > current_best_student["score"]:
    current_best_student["score"] = student["score"]
    current_best_student["name"] = student["name"]

print(current_best_student)
    
"""""
Part 2: Mini-Project — Student Roster Analyzer
A data file is provided in week-4/data/roster.py. Copy the students list from that file into your script — it contains dictionaries with name, score, and subject fields.
Using loops and data structure operations, your script must:
1.Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
2.Calculate the class average — accumulate the total score in a loop, then divide.
3.List all unique subjects — use a set to collect subjects as you loop, then print them.
4.List high scorers — use a loop and .append() to get the names of all students who scored above 75.
"""""

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer:  loop through the list and track the highest score and
#  the name that goes with it.

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

print(f"The student with the highest grade is{current_best_student['name']} with a score of {current_best_student['score']}.")
    

# Calculate the class average: accumulate the total score in a loop, then divide.
 # to get the average, take all scores and divide by the number of scores 
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

score_count = len(students)
total = 0 
for student in students:  
    score = student["score"]
    total = total + score
class_average = total / score_count
print(f"The class average is {class_average:.2f}.")

# List all unique subjects 
students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

class_subjects = []
for student in students: 
    subject = student["subject"]
    class_subjects.append(subject)
print(f"The unique subjects in the class are: {', '.join(set(class_subjects))}.")

# List high scorers use a loop and .append() to get the names of all students who scored above 75.

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]


high_scorers = []
for student in students:
    score = student["score"]
    if student["score"] > 75:
        high_scorers.append(student["name"])
print(f"The highest scoring students who scored above a 75 are: {', '.join(high_scorers)}.")
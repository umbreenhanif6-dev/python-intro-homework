"""
Write a program that analyzes this data and writes a formatted report to a new file. 
Follow these steps:
Use os.path.exists() to verify that ../data/expenses.csv exists before opening it.
If it doesn't, print an error message and stop.
"""
import os
import csv
import datetime

file_path = '../data/expenses.csv'
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else: 
    print(f"The file '{file_path}' does not exist.")
    exit()

# read the csv file into a list of dictionaries

expenses = []
with open(file_path, "r") as file: 
    reader = csv.DictReader(file)

    for entry in reader: 
        expenses.append(entry)

#Convert the amount field to float for each row.
    for expense in expenses:
        expense['amount'] = float(expense['amount'])
    print(expenses, "\n")

#Filter the list to only rows where category is "Food".
food_expenses = []
for entry in expenses: 
    if entry["category"] == "Food":
       food_expenses.append(entry) 
print(food_expenses) 

# Calculate the total amount spent on Food.
total = 0

for entry in expenses:
    if entry["category"].strip().lower() == "food":
        total += entry["amount"]

print(f"The total for Food is ${total:.2f}.")

d = datetime.date.today()

with open("food_report.txt", "w") as file:
    file.write(
        f"Food Expense Report - generated {d.strftime('%B %d, %Y')}\n\n"
    )

    for entry in expenses:
        if entry["category"].strip().lower() == "food":
            file.write(f"{entry['date']}: ${entry['amount']:.2f}\n")

    file.write(f"Total: ${total:.2f}\n")
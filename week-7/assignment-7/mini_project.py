"""
Write a program that analyzes this data and writes a formatted report to a new file. 
Follow these steps:
Use os.path.exists() to verify that ../data/expenses.csv exists before opening it.
If it doesn't, print an error message and stop.
"""


import os
import csv

file_path = '../data/expenses.csv'
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else: 
    print(f"The file '{file_path}' does not exist.")

"""
Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
Convert the amount field to float for each row.
Filter the list to only rows where category is "Food".
Calculate the total amount spent on Food.
"""
""" read the csv file and print its contents as is: 
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    file.close()"""

# read the csv file into a list of dictionaries

expenses = []
with open(file_path, "r") as file: 
    reader = csv.DictReader(file)

    for entry in reader: 
        expenses.append(entry)
  #  print(expenses)
  #Convert the amount field to float for each row.
    for expense in expenses:
        expense['amount'] = float(expense['amount'])
    print(expenses)
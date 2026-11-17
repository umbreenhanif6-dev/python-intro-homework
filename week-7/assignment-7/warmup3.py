import os
print(os.getcwd())

if os.path.exists("C:\\Umbreen\\python-intro-homework\\week-7\\data\\expenses.csv"):
    print("expenses.csv found.") #added period at the end of the string
else:
    print("expenses.csv not found.")

path = os.path.join("..", "data", "expenses.csv")
print(path)
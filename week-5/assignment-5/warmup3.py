"""
Warmup 3: Linear Search Save as: warmup3.py
Start with a hardcoded list of names. Ask the user to enter a name. Loop through the list and print whether the name was found and at what index — or a not-found message if it isn't in the list. The examples below show the format for two different searches — your names, index, and message wording might differ:
Do not use Python's .index() method or the in operator — implement the search yourself with a loop.
Enter a name to search for: Marcus
Found "Marcus" at index 3.

Enter a name to search for: Zara
"Zara" was not found in the list.
"""

students = [
    "James", "Afan", "Gerald", "Holly", "Jayla", "Charlie"
]

name_request = input("Enter a name to search for: ").strip()

for index, name in enumerate(students):
    if name_request.lower() == name.lower():
        print(f'Found "{name}" at index {index}.')
        break
else:
    print(f'"{name_request}" was not found in the list.')

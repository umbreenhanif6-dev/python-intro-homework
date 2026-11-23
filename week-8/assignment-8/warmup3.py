"""
Warmup 3: Handle a Missing File
Write a script that attempts to open ../data/missing.txt
 (this file does not exist). Use try/except FileNotFoundError to catch the error 
 and print a helpful message rather than a traceback. The example below shows the format — your message wording might differ:
Error: "missing.txt" was not found. Please check the file path and try again.
"""

try:
    with open("../data/missing.txt", "r") as file: 
        contents = file.read() 
        print(contents)
except FileNotFoundError: 
    print("This file is not found. Check the file path and try again.")
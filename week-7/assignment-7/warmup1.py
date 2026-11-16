with open("week-7\\data\\notes.txt", "r") as file: 
    for number, line in enumerate(file):
        print(f"Line {number + 1}: {line.strip()}")
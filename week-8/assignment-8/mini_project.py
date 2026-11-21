import os
import csv

clean_data = []
skipped_rows = []
attempted = 0
parsed = 0
skipped = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=1):
            attempted += 1 

            if None in row:
                skipped_rows.append({
                    "row": row_number ,
                    "reason": "Extra column detected."
                })
                skipped += 1

            else: 
                if not row["name"].strip() or not row["category"].strip() or not row["amount"].strip():
                    skipped_rows.append({
                    "row": row_number,
                    "reason": "Missing or blank field."
                    })
                skipped += 1
                
            else:
                try:
                    new_row = {
                    "name": row["name"],
                    "category": row["category"],
                    "amount": float(row["amount"])
                    }

                    clean_data.append(new_row)
                    parsed += 1

                except ValueError:
                    skipped_rows.append({
                        "row": row_number ,
                        "reason": "Could not convert entry to float."})
                    skipped += 1
                except KeyError:
                    skipped_rows.append({
                        "row": row_number ,
                        "reason": "Missing expected column."})
                    skipped += 1 
            print("File exists.")
            print("Rows attempted:", attempted)
            print("Rows parsed:", parsed)
            print("Rows skipped:", skipped)   
            print("Skipped row details: ")
            for item in skipped_rows:
                print(item)

except FileNotFoundError:
    print("File is not found. Please check the file location.")
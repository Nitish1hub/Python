# Create a program to:
# ● Open reviews.json
# ● If missing → log "FileNotFoundError" to error_log.txt
# ● If corrupted → catch JSONDecodeError

import json
try:
    with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\reviews.json", "r") as infile:
        reviews = json.load(infile)
        with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\processed_reviews.txt", "w") as outfile:
            for review in reviews:
                print(reviews[review])  # Optional: Print to console
                cleaned_review = review.strip().lower()
                print(cleaned_review)  # Optional: Print to console
                outfile.write(cleaned_review + "\n")
except FileNotFoundError:
    with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\error_log.txt", "a") as error_log:
        error_log.write("FileNotFoundError: reviews.json not found\n")
except json.JSONDecodeError:
    with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\error_log.txt", "a") as error_log:
        error_log.write("JSONDecodeError: reviews.json is corrupted\n")

# Sample Output in error_log.txt:
# FileNotFoundError: reviews.json not found
# JSONDecodeError: reviews.json is corrupted
# Sample Output :
# 4.8
# u101
# 3.2
# u102
# 4.6
# u103
# 2.8
# u104
# 4.0
# u105
# in processed_reviews.txt
# u101
# u102
# u103
# u104
# u105

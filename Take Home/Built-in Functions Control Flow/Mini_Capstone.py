# ○ Read from raw_reviews.txt
# ○ Clean reviews (strip + lower)
# ○ Store as list
# ○ Save to cleaned_reviews.json
# ○ Handle file or key errors gracefully


import json
try:
    with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\raw_reviews.txt", 'r') as file:
        reviews = file.readlines()
    
    cleaned_reviews = [review.strip().lower() for review in reviews]
    
    with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\cleaned_reviews.json", 'w') as json_file:
        json.dump(cleaned_reviews, json_file)
    
    print("Cleaned reviews have been saved to cleaned_reviews.json")

except FileNotFoundError:
    print("Error: The file raw_reviews.txt was not found.")
except KeyError as e:
    print(f"Key error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
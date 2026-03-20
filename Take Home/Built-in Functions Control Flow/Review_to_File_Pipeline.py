# Steps:
# 1. Read reviews from user_input.txt.
# 2. Clean and lowercase them.
# 3️. Write to processed_reviews.txt.

with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\user_input.txt", "r") as infile:
    lines = infile.readlines()
    lowercase_lines = [line.strip().lower() for line in lines]
with open("C:\\_Projects\\Personal\\Python\\Take Home\\Built-in Functions Control Flow\\processed_reviews.txt", "w") as outfile:
    for line in lowercase_lines:
        print(line)  # Optional: Print to console
        outfile.write(line + "\n")

# Sample Output

# good
# excellent scooter!
# average
# outstanding battery backup!
# buy now and save big!
# fast response and friendly support
# limited time offer! don't miss out
# comfortable seat and smooth ride
# poor build quality, breaks soon
# battery life is amazing, lasts long
# delivery was late
# amazing value for money
# buy one get one free
# decent performance for city rides
# terrible customer care, not helpful
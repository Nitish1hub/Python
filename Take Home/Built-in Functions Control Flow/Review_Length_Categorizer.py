# Review Length Categorizer
# reviews = ["Good", "Excellent scooter!", "Average", "Outstanding battery backup!"]
# For each review:
# ● If len < 10 → “Short”
# ● If 10–25 → “Medium”
# ● If len > 25 → “Detailed”
# Print summary counts for each category.

reviews = ["Good", "Excellent scooter!", "Average", "Outstanding battery backup!"]
short_count = 0
medium_count = 0
detailed_count = 0
for review in reviews:
    length = len(review)
    if length < 10:
        short_count += 1
    elif 10 <= length <= 25:
        medium_count += 1
    else:
        detailed_count += 1

print(f"Short: {short_count}, Medium: {medium_count}, Detailed: {detailed_count}")

# Sample output:
# Short: 2, Medium: 1, Detailed: 1

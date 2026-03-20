# Combine everything into a short script:
#   • Store 4 ratings
#   • Print:
#     o Count of ratings
#     o Average (rounded to 2 decimals)
#     o Highest rating
#     o Sentiment label (if/elif/else)
#     o Formatted summary line with f-string

ratings = [4.5, 3.0, 5.0, 4.0]
count = len(ratings)
average = round(sum(ratings) / count, 2)
highest = max(ratings)
if average >= 4.5:
    sentiment = "Excellent"
elif average >= 3.0:
    sentiment = "Good"
else:
    sentiment = "Needs Improvement"
summary = f"Count: {count}, Average: {average}, Highest: {highest}, Sentiment: {sentiment}"
print(summary)

# Sample output:
# Count: 4, Average: 4.13, Highest: 5.0, Sentiment: Good

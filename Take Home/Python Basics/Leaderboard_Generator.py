# Given:
# scores = [86, 92, 78, 90, 99]
#   • Sort the scores descending (sorted(..., reverse=True))
#   • Print top 3 scorers in one line using f-string

scores = [86, 92, 78, 90, 99]
sorted_scores = sorted(scores, reverse=True)
print(f"Sorted scores (descending): {sorted_scores}")
top_3 = sorted_scores[:3]
print(f"Top 3 scorers: {top_3[0]}, {top_3[1]}, {top_3[2]}")

# Sample Output: 
# Sorted scores (descending): [99, 92, 90, 86, 78]
# Top 3 scorers: 99, 92, 90

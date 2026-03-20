# Sales Sentiment Tracker
# Given:
# ratings = [4.9, 4.2, 3.1, 4.6, 2.8]
# Compute:
#   • Count of reviews (len)
#   • Sum of all ratings (sum)
#   • Average (round)
# Print a summary line:
# “Out of 5 reviews, average sentiment is 3.92.”

ratings = [4.9, 4.2, 3.1, 4.6, 2.8]
print("Ratings:", ratings)
print("Total ratings:", len(ratings))
print("Sum of ratings:", sum(ratings))
print("Average rating:", round(sum(ratings) / len(ratings), 2))
print(f"Out of {len(ratings)} reviews, average sentiment is {round(sum(ratings) / len(ratings), 2)}.")

# Sample Output:
# Ratings: [4.9, 4.2, 3.1, 4.6, 2.8]
# Total ratings: 5
# Sum of ratings: 19.6
# Average rating: 3.92
# Out of 5 reviews, average sentiment is 3.92.
# Write a program that:
#  • Takes 5 numeric ratings from user input
#  • Prints the highest, lowest, and the absolute difference between them

ratings= input("Enter 5 ratings (1-10) separated by ',': ")
ratings_list = list(map(float, ratings.split(",")))
print("Ratings:", ratings_list)
max_rating = max(ratings_list)
min_rating = min(ratings_list)
print("Max rating:", max_rating)
print("Min rating:", min_rating)
print("Average rating:", sum(ratings_list) / len(ratings_list))
print("Absolute difference between max and min:", abs(max_rating - min_rating))

# Sample Output:
# Enter 5 ratings (1-10) separated by ',': 3.5,4.8,9.7,10,3.3
# Ratings: [3.5, 4.8, 9.7, 10.0, 3.3]
# Max rating: 10.0
# Min rating: 3.3
# Average rating: 6.26
# Absolute difference between max and min: 6.7
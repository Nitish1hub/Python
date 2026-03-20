# Formatted Feedback Summary
# Ask the user for their name and rating.
# Display output in both styles:
# Riya rated the product 4.5 stars.
# Riya rated the product 4.50 stars

name = input('Enter your name : ')
rating = float(input('Enter your rating (1-10) : '))
print(f"{name} rated the product {rating:.1f} out of 10.")
print(f"{name} rated the product {rating:.2f} out of 10.")

# Sample Output:
# Enter your name : Riya
# Enter your rating (1-10) : 4.5
# Riya rated the product 4.5 out of 10.
# Riya rated the product 4.50 out of 10.

# Notes: While round() works well for many things, it has a small quirk: if the number doesn't need extra decimals, it won't show them. For example, round(4.5, 3) will still just display 4.5 instead of 4.500
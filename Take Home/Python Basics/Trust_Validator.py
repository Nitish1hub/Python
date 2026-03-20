# Ask user:
# rating = float(input("Rating: "))
# verified = input("Verified (y/n): ")
# If verified == "y":
#   • If rating ≥ 4 → “Trusted Positive Review”
#   • Else → “Trusted Negative Review”
# Else → “Unverified Review”

rating = float(input("Rating: "))
verified = input("Verified (y/n): ")
if verified == "y":
    if rating >= 4:
        print("Trusted Positive Review")
    else:
        print("Trusted Negative Review")
else:
    print("Unverified Review")

# Sample Output:
# Rating: 4.5
# Verified (y/n): y
# Trusted Positive Review
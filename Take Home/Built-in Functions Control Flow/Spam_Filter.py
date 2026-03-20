# reviews = ["Buy now and save!", "Good performance", "Limited time offer!", "Fast response"]
# ● Skip reviews containing “buy” or “offer”.
# ● Store valid reviews in a list.
# ● Print cleaned list.

reviews = ["Buy now and save!", "Good performance", "Limited time offer!", "Fast response"]
cleaned_reviews = []
for review in reviews:
    if "buy" in review.lower() or "offer" in review.lower():
        continue
    cleaned_reviews.append(review)

print(cleaned_reviews)

# Sample output:
# ['Good performance', 'Fast response']

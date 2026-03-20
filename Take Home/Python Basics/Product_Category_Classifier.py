# Input rating and product type (Electronics or Clothing):
#   • If rating ≥ 4.5 → “Highly Recommended [category]”
#   • Else if rating ≥ 3.5 → “Satisfactory [category]”
#   • Else → “Needs Improvement [category]”

input_rating = float(input("Enter the product rating (0-5): "))
input_category = input("Enter the product category (Electronics/Clothing): ")
if input_rating >= 4.5:
    print(f"Highly Recommended {input_category}")
elif input_rating >= 3.5:
    print(f"Satisfactory {input_category}")
else:
    print(f"Needs Improvement {input_category}")

# Sample output:
# Enter the product rating (0-5): 4.3
# Enter the product category (Electronics/Clothing): Cloathing
# Satisfactory Cloathing

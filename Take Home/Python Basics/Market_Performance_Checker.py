# Given two products’ average ratings:
# p1 = 4.6
# p2 = 4.3
# Print the better one using:
# "Product 1 performs better (4.6 vs 4.3)"
# If equal, print “Both perform equally.”
# (Covers: conditional logic + formatting)

p1 = 4.6
p2 = 4.3
if p1 > p2:
    print(f"Product 1 performs better ({p1} vs {p2})")
elif p2 > p1:
    print(f"Product 2 performs better ({p2} vs {p1})")
else:    
    print("Both perform equally.")

# Sample Output: Product 1 performs better (4.6 vs 4.3)

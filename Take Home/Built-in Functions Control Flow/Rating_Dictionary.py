# users = ["U101","U102","U103"]
# ratings = [4.8,3.2,4.6]
# 
# ● Create a dictionary mapping users → ratings.
# ● Print all keys and values separately.
# ● If any rating < 3️ → print "Needs attention".

users = ["U101","U102","U103"]
ratings = [4.8,3.2,4.6]
user_ratings = dict(zip(users, ratings))
for user, rating in user_ratings.items():
        print(f"{user}: {rating}")
print("Users:", user_ratings.keys())
print("Ratings:", user_ratings.values())

for user, rating in user_ratings.items():
    if rating < 3:
        print(f"User {user} needs attention.")

# Sample Output:
# Users: dict_keys(['U101', 'U102', 'U103'])
# Ratings: dict_values([4.8, 3.2, 4.6

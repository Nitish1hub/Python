# Why is round(4.675, 2) → 4.67 and not 4.68?
# Explain how floating-point rounding works in Python.

round(4.675, 2)
# Output: 4.67
# In Python, floating-point numbers are represented in binary, which can lead to small precision errors.
# The number 4.675 cannot be represented exactly in binary, so it is stored as a value slightly less than 4.675.
# When rounded to 2 decimal places, this small difference causes the result to be 4.67 instead of 4.68.

"""Write a program that counts how many times each grade appears in the list and prints the results."""
import pandas as pd
# Your solution for Question 4
grades = [85, 92, 78, 90, 92, 85, 92]

# Write your code to count occurrences
# We are using pandas for simplicity and efficiency. Pandas series has a built-in method value_counts() that does exactly this.
grade_series = pd.Series(grades)
print(grade_series)

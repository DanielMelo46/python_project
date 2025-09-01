"""You are given a list of numbers. 
Write a Python program that loops through the list and prints whether each number is even or odd."""
# Your solution for Question 2
numbers = [10, 21, 32, 43, 54]

# Write your loop here
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
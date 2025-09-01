"""You are given a sentence: "Python is fun and powerful". Write a Python program that 
checks whether the word "fun" or "boring" is in the sentence. Print different messages 
depending on whether the word is found or not. Be sure to test your program with different 
sentences to ensure correct results."""

# Your solution for Question 3
sentence = 'Python is boring and powerful'

# Check for words 'fun' and 'boring'
if 'fun' in sentence:
    print("The word 'fun' is in the sentence.")
if 'boring' in sentence:
    print("The word 'boring' is in the sentence.")
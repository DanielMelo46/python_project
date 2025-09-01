"""You are given a dictionary that contains information about different countries and their populations in millions.
Write a program that loops over the dictionary and prints the name of each country and its population. 
If the population is over 100 million, print a message saying the country is "heavily populated."""

countries = {
    "Canada": 38,
    "Brazil": 212,
    "India": 1391,
    "Germany": 83,
    "Japan": 126
}
# Write your loop here
for c , p in countries.items():# Iterating over the items, which works as a pair of iterators for key and value
    print(f"Country: {c}, population: {p} million(s).")
    if p > 100:
        print(f"{c} is heavily populated.")

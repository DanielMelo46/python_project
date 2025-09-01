# Example 3
def calculate_discounted_price(price : float = 0.0, discount : float = 0.0) -> float:
    """Calculate the price after a discount."""
    if discount < 0 or discount > 1:
        print("Error: Discount must be between 0 and 1.")
        return price
    return price * (1 - discount )

calculate_discounted_price(100, 0.10)  # Example usage
"""# Calculate discount for customer 1
price1 = 100
discount1 = 0.10
final_price1 = price1 - (price1 * discount1)

# Calculate discount for customer 2
price2 = 250
discount2 = 0.15
final_price2 = price2 - (price2 * discount2)

# Calculate discount for customer 3
price3 = 50
discount3 = 0.05
final_price3 = price3 - (price3 * discount3)

print(f"Final price for customer 1: ${final_price1}")
print(f"Final price for customer 2: ${final_price2}")
print(f"Final price for customer 3: ${final_price3}")"""
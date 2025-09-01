# Example 3
def calculate_discounted_price(price : float = 0.0, discount : float = 0.0) -> float:
    """Calculate the price after a discount."""
    if discount < 0 or discount > 1:
        print("Error: Discount must be between 0 and 1.")
        return price
    return price * (1 - discount )

print(f"Final price for customer 1: ${calculate_discounted_price(100.0, 0.1)}")
print(f"Final price for customer 2: ${calculate_discounted_price(250.0, 0.15)}")
print(f"Final price for customer 3: ${calculate_discounted_price(50.0, 0.05)}")
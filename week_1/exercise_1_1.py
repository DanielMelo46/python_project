# Example 1
def area_rectangle(length : float = 0.0, width : float = 0.0) -> float:
    """Calculate the area of a rectangle."""
    return length * width

def area_circle(radius : float = 0.0) -> float:
    """Calculate the area of a circle using an approximate valie of pi."""
    return 3.14 * radius ** 2

# Example 2
def print_is_odd_or_even(number : int = 0) -> None:
    """Print if a number is odd or even. This function is used by list_odd_or_even_check."""
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

def list_odd_or_even_check(numbers : list[int] = []) -> None:
    """Check if numbers in a list are odd or even."""
    for number in numbers:
        print_is_odd_or_even(number)

# Example 3

def calculate_discounted_price(price : float = 0.0, discount : float = 0.0) -> float:
    """Calculate the price after a discount."""
    if discount < 0 or discount > 1:
        print("Error: Discount must be between 0 and 1.")
        return price
    return price * (1 - discount )
# Calculating area of rectangles
length1 = 10
width1 = 5
area_rectangle1 = length1 * width1

length2 = 15
width2 = 7
area_rectangle2 = length2 * width2

# Calculating area of circles
radius1 = 4
area_circle1 = 3.14 * (radius1 ** 2)

radius2 = 6
area_circle2 = 3.14 * (radius2 ** 2)

print("Area of first rectangle:", area_rectangle1)
print("Area of second rectangle:", area_rectangle2)
print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)
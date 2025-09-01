# Example 1
def area_rectangle(length : float = 0.0, width : float = 0.0) -> float:
    """Calculate the area of a rectangle."""
    return length * width

def area_circle(radius : float = 0.0) -> float:
    """Calculate the area of a circle using an approximate valie of pi."""
    return 3.14 * radius ** 2

# Calculating area of rectangles
# Note the use of dictionaries to store rectangle properties
rectangle1 = {'length': 10, 'width': 5}
rectangle2 = {'length': 20, 'width': 10}
circle1 = 5.0 # radius
circle2 = 10.0 # radius

print(f"Area of rectangle 1: {area_rectangle(rectangle1['length'], rectangle1['width'])}")
print(f"Area of rectangle 2: {area_rectangle(rectangle2['length'], rectangle2['width'])}")
print(f"Area of circle 1: {area_circle(circle1)}")
print(f"Area of circle 2: {area_circle(circle2)}")
# Example 1
def area_rectangle(length : float = 0.0, width : float = 0.0) -> float:
    """Calculate the area of a rectangle."""
    return length * width

def area_circle(radius : float = 0.0) -> float:
    """Calculate the area of a circle using an approximate valie of pi."""
    return 3.14 * radius ** 2

# Calculating area of rectangles
# Note the use of dictionaries to store rectangle properties
rectangles = [
    {'name' : 'R1','length': 10, 'width': 5},
    {'name' : 'R2','length': 20, 'width': 10}
]

for rectangle in rectangles:
    # calculate the area
    area = area_rectangle(rectangle["length"], rectangle["width"])
    # print the output
    print(f"Area of {rectangle["name"]} rectangle: {area}")

circles = [
    {'name' : 'C1', 'radius' : 4},
    {'name' : 'C2', 'radius' : 6}
]

for circle in circles :
    #Calculation
    area = area_circle(circle['radius'])
    #print the output
    print(f'Area of {circle['name']} : {area}')
    
# print(f"Area of circle 1: {area_circle(circle1)}")
# print(f"Area of circle 2: {area_circle(circle2)}")
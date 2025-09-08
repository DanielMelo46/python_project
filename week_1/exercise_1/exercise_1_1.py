# Example 1
def area_rectangle(length : float = 0.0, width : float = 0.0) -> float:
    """Calculate the area of a rectangle."""
    return length * width

def area_circle(radius : float = 0.0) -> float:
    """Calculate the area of a circle using an approximate valie of pi."""
    return 3.14 * radius ** 2

rectangles = [
    {'name' : 'R1','length': 10, 'width': 5},
    {'name' : 'R2','length': 20, 'width': 10}
]

circles = [
    {'name' : 'C1', 'radius' : 4},
    {'name' : 'C2', 'radius' : 6}
]


shapes = [
    {'name' : 'Circle', 'instances' : circles},
    {'name' : 'Rectangle', 'instances' : rectangles}
]

for shape in shapes:
    shape_name = shape['name']
    instances = shape['instances']
    for instance in instances:
        if shape_name == 'Circle':
            area = area_circle(instance['radius'])
            print(f"Area of {instance['name']} : {area}")
        else:
            area = area_rectangle(instance['length'], instance['width'])
            print(f"Area of {instance['name']} : {area}")
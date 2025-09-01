# Question 3
def transform_to_dict_3(text : str = "") -> dict:
    """Transform a string of several key-value pairs (several char cases) separated by ; into a list of dictionaries."""
    result = []
    chars = [':', '=', '-'] # List of possible characters that can separate key and value
    persons = text.split(';')
    for person in persons:
        person_dict = {} # This dict will save each person's attributes
        pairs = person.split(',')
        for pair in pairs :
            for char in chars:
                if char in pair:
                    k , v = pair.split(char,1)
                    person_dict[k.strip()] = v.strip()
                    break # Exit the loop once a match is found
        result.append(person_dict)
    return result

# messy data string
data = "product_name: Laptop, price = $999, brand - Dell ; product_name: Smartphone, price: $599 , brand = Samsung ; product_name - Tablet , price=299,brand : Apple"

# expected output
[
    {'product_name': 'Laptop', 'price': '$999', 'brand': 'Dell'},
    {'product_name': 'Smartphone', 'price': '$599', 'brand': 'Samsung'},
    {'product_name': 'Tablet', 'price': '299', 'brand': 'Apple'}
]
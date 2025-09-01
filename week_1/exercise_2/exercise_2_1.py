
# Question 1
def transform_to_dict(text : str = "") -> dict:
    """Transform a string of key-value pairs into a dictionary."""
    result = {}
    pairs = text.strip().split(';')
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1) # In case there are multiple colons
            result[key.strip().lower()] = value.strip() # Remove leading/trailing whitespace
    return result

# input string
data = " Name: John Doe ; Age : 25;  CITY: New York ; Occupation: Software Engineer "

print('Question 1')
data = " Name: John Doe ; Age : 25;  CITY: New York ; Occupation: Software Engineer "
print(f'Before: {data}')
transformed_dict = transform_to_dict(data)
print(f'After: {transformed_dict}')
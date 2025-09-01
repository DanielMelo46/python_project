# Question 2
def transform_to_dict_2(text : str = "") -> dict:
    """Transform a string of several key-value pairs separated by a pipe into a list of dictionaries.
    Each person's attributes are separated by a comma.
    """
    result = []
    persons = text.strip().split('|')
    for person in persons:
        person_dict = {} # This dict will save each person's attributes
        pairs = person.split(',',1)
        for pair in pairs :
            k , v = pair.split(':',1)
            person_dict[k.strip()] = v.strip()
        result.append(person_dict)
    return result

# input
data2 = "Name: Alice, Age: 30, City: Los Angeles | Name: Bob, Age: 25, City: Chicago | Name: Charlie , Age: 35, City: New York"

print('Question 2')
data2 = "Name: Alice, Age: 30, City: Los Angeles | Name: Bob, Age: 25, City: Chicago | Name: Charlie , Age: 35, City: New York"
print(f'Before: {data2}')
print(f'After: {transform_to_dict_2(data2)}') # List of dictionaries
def transform_to_dict_6(text : str = "") -> dict:
    """Transform a string of several key-value pairs (several char) separated by ; into a list of dictionaries."""
    result = []
    expected_keys = ['transaction_id', 'customer_name', 'item', 'price', 'discount']
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
        # Ensure all expected keys are present
        for key in expected_keys:
            if key not in person_dict:
                person_dict[key] = None
    return result

# messy data string
data6 = "transaction_id:001, customer_name: Alice, item=Laptop, price: $999; transaction_id=002, customer_name: Bob, item - Smartphone, price= $599; transaction_id:003, item=Tablet, price:299, discount-10%; transaction_id=004, customer_name=Charlie, item: Headphones, discount=5%"

print('Question 6')
data6 = "transaction_id:001, customer_name: Alice, item=Laptop, price: $999; transaction_id=002, customer_name: Bob, item - Smartphone, price= $599; transaction_id:003, item=Tablet, price:299, discount-10%; transaction_id=004, customer_name=Charlie, item: Headphones, discount=5%"
print(f'Before: {data6}')
print(f'After: {transform_to_dict_6(data6)}')
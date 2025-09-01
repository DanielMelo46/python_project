def transform_to_dict_5(text : str = "") -> dict:
    """Transform a string of several key-value pairs separated by a pipe into a list of dictionaries."""
    result = []
    entries = text.strip().split('|')
    for entry in entries:
        person_dict = {} # This dict will save each person's attributes
        pairs = entry.split(',')
        for pair in pairs :
            k , v = pair.split(':')
            person_dict[k.strip()] = None if v.strip == 'N/A' else v.strip()
        result.append(person_dict)
    return result

# messy data string
data = "device_id: 001, temp: 72, humidity: 45 | device_id: 002, temp: N/A, humidity: 50 | device_id: 003, temp: 68, humidity: N/A"

# expected output
[
    {'device_id': '001', 'temp': 72, 'humidity': 45},
    {'device_id': '002', 'temp': None, 'humidity': 50},
    {'device_id': '003', 'temp': 68, 'humidity': None}
]
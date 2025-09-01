import re
# Question 4
def transform_to_dict_4(text : str = "") -> dict:
    """Transform a string of several key-value pairs separated by a pipe into a list of dictionaries.
    Each person's attributes are separated by a comma. The roles attribute can have multiple values separated by a comma.
    This function implements regex to handle the roles attribute correctly."""
    result = []
    entries = text.strip().split('|')
    for entry in entries:
        # Replacing the roles comma with ' @ ' to avoid splitting on it
        person_dict = {}
        entry = re.sub(r'(roles:\s*\w+)\s*,\s*(\w+)', r'\1 @ \2', entry)
        parts = [part.strip() for part in entry.strip().split(',')]
        for pair in parts :
            k , v = pair.split(':',1)
            person_dict[k.strip()] = [vi.strip() for vi in v.split('@')] if  k == 'roles' else v.strip()
        result.append(person_dict)
    return result

# messy data string
data = "employee_name: Sarah, department: HR, roles: recruiter, trainer | employee_name: Mike , department: Engineering , roles: developer, team lead | employee_name: Alice , department: HR , roles: recruiter"

# expected output
[
    {
        'employee_name': 'Sarah',
        'department': 'HR',
        'roles': ['recruiter', 'trainer']
    },
    {
        'employee_name': 'Mike',
        'department': 'Engineering',
        'roles': ['developer', 'team lead']
    },
    {
        'employee_name': 'Alice',
        'department': 'HR',
        'roles': ['recruiter']
    }
]
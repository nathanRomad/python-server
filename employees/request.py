EMPLOYEES = [
    {
      "id": 1,
      "name": "Charles Schulz",
      "position": "CEO",
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Cesar Millan",
      "position": "Dog Whisperer",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Snoop Dogg",
      "position": "Director of Marketing & Social Media",
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Jackson Galaxy",
      "position": "Cat Whisperer",
      "locationId": 1
    },
    {
      "id": 5,
      "name": "Orlando Bloom",
      "position": "CEO",
      "locationId": 2
    },
    {
      "id": 6,
      "name": "Victoria Stillwell",
      "position": "Dog Whisperer",
      "locationId": 2
    },
    {
      "id": 7,
      "name": "Gary Fleck",
      "position": "Director of Marketing & Social Media",
      "locationId": 2
    },
    {
      "id": 8,
      "name": "Harlan Pepper",
      "position": "Cat Whisperer",
      "locationId": 2
    }
]

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def get_all_employees():
    return EMPLOYEES
ANIMALS = [
    {
      "id": 1,
      "name": "Nanook",
      "breed": "Siberian Husky",
      "customerId": 1,
      "locationId": 1
    },
    {
      "id": 2,
      "name": "Frank",
      "breed": "Brown Tabby",
      "customerId": 2,
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Dean",
      "breed": "Brown Tabby",
      "customerId": 2,
      "locationId": 1
    },
    {
      "id": 4,
      "name": "Gator",
      "breed": "German Shepherd",
      "customerId": 1,
      "locationId": 1
    },
    {
      "id": 5,
      "name": "Rubber Duckie",
      "breed": "Rubber Duck",
      "customerId": 1,
      "locationId": 2
    },
    {
      "id": 6,
      "name": "Mighty",
      "breed": "Labradoodle",
      "customerId": 3,
      "locationId": 2
    },
    {
      "id": 7,
      "name": "Robo-dog",
      "breed": "robotDog_v2.0",
      "customerId": 4,
      "locationId": 2
    }
]

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def get_all_animals():
    return ANIMALS
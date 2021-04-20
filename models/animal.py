class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.locationId = location_id
        self.customerId = customer_id
        self.location = None
        self.customer = None

new_animal = Animal(8, "Snickers", "Dog", "Recreation", 1, 4)

# print(new_animal.name)